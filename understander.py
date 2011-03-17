#!/usr/bin/env python3
#from __future__ import print_function
from linkgrammar import lp, Sentence, Linkage #,clg,ParseOptions,Dictionary
from understanding import conversation, infinitive, adverb, stripSub
#import linkgrammar
#import os
#import subprocess
#import festival

def findProblems(linkage,sent):
    for i, word in enumerate(linkage.get_words()):
        index=word.find('[~]')
        if index>-1:
            print("I am assuming '"+sent[i]+"' should be '"+word.replace('[~]','')+"'.")
        index=word.find('[?]')
        if index>-1:
            print("I do not recognize '"+sent[i]+"'.")
        index=word.find('[!]')
        if index>-1:
            print("I do not recognize '"+sent[i]+"'.")
    

def parseString(s,debug):
    sent = Sentence(s)
    if sent.parse():
        linkage = Linkage(0,sent)
        if debug:
            linkage.print_diagram()
        findProblems(linkage, sent)
        return linkage
    else:
        return None

def parseLinkage(linkage):
    links={}
    words={}
    for link in linkage:
        key="".join(char for char in link.label if char.isupper())
        subscript="".join(char for char in link.label if not char.isupper())
        if key in links.keys():
            if subscript in links[key].keys():
                links[key][subscript].append((link.lword,link.rword,link.domain_names))
            else:
                links[key][subscript]=[(link.lword,link.rword,link.domain_names)]
        else:
            links[key]={subscript:[(link.lword,link.rword,link.domain_names)]}
        if link.lword in words.keys():
            words[link.lword].append((key,subscript))
        else:
            words[link.lword]=[(key,subscript)]
        if link.rword in words.keys():
            words[link.rword].append((key,subscript))
        else:
            words[link.rword]=[(key,subscript)]
    del link
    return links,words

parser = lp()

current=conversation()

#talker=festival.open()

while True:
    s=input()
    linkage=parseString(s, True)
    if linkage:
        try:
            links,words=parseLinkage(linkage)
            
            #print links
            combinations=dict((key,key) for key in words)
            #figure out a way to treat the versions that start with "ID"
            #remove spacer variable
            for name in ('AN','G','ND','TM','TW','TY'): #combine some two-word items together
                if name in links:
                    for group in links[name].values():
                        for link in group:
                            lkey=link[0]
                            left=combinations[lkey]
                            rkey=link[1]
                            right=combinations[rkey]
                            combination=stripSub(left)+' '+stripSub(right)
                            for key in combinations:
                                if combinations[key]==left or combinations[key]==right:
                                    combinations[key]=combination
            for name in ('YP','YS'):    #drop the 's of possessives
                if name in links:
                    for group in links[name].values():
                        for link in group:
                            for key in combinations:
                                if combinations[key]==combinations[link[1]]:
                                    combinations[key]=combinations[link[0]]
            if 'D' in links:    #combine determiners to noun
                for group in links['D'].values():
                    for link in sorted(group):
                        dlink=link[0]
                        detr=combinations[dlink]
                        nlink=link[1]
                        noun=combinations[nlink]
                        if str(detr) in ('a','an','the'):
                            combination=current.new(detr,noun)
                        else:
                            combination=current.possession(detr,noun)
                        for key in combinations:
                            if combinations[key]==noun or combinations[key]==detr:
                                combinations[key]=combination
            if 'A' in links:    #apply adjectives before the rest of the sentence is parsed
                for group in links['A'].values():
                    for link in sorted(group,reverse=True):
                        akey=link[0]
                        adj=combinations[akey]
                        nkey=link[1]
                        noun=combinations[nkey]
                        combination=current.adjective(adj,noun)
                        for key in combinations:
                            if combinations[key]==noun or combinations[key]==detr:
                                combinations[key]=combination
            
            if 'Q' in links or 'W' in links and any(char in links['W'] for char in "qsj"):
                #print "interogative sentence"
                if 'S' in links:
                    SV=links['S']
                    subject=SV[list(SV.keys())[0]][0][0]
                    verb=SV[list(SV.keys())[0]][0][1]
                elif 'SI' in links:
                    SV=links['SI']
                    subject=SV[list(SV.keys())[0]][0][1]
                    verb=SV[list(SV.keys())[0]][0][0]
                elif 'SXI' in links:
                    SV=links['SXI']
                    subject=SV[list(SV.keys())[0]][0][1]
                    verb=SV[list(SV.keys())[0]][0][0]
                verbLinks=words[verb]
                subject=combinations[subject]
                verb=combinations[verb]
                if any(tups[0]=='O' for tups in verbLinks):
                    directObject=links['O'][[tups for tups in verbLinks if tups[0]=='O'][0][1]][0][1]
                    directObject=combinations[directObject]
                    directObject=current[directObject]
                elif any(tups[0]=='P' for tups in verbLinks):
                    directObject=links['P'][[tups for tups in verbLinks if tups[0]=='P'][0][1]][0][1]
                    directObject=combinations[directObject]
                    directObject=current[directObject]
                elif any(tups[0]=='I' for tups in verbLinks):
                    inf=links['I'][[tups for tups in verbLinks if tups[0]=='I'][0][1]][0][1]
                    infLinks=words[inf]
                    inf=combinations[inf]
                    if any(tups[0]=='O' for tups in infLinks):
                        directObject=links['O'][[tups for tups in infLinks if tups[0]=='O'][0][1]][0][1]
                    elif any(tups[0]=='B' for tups in infLinks):
                        directObject=links['B'][[tups for tups in infLinks if tups[0]=='B'][0][1]][0][0]
                    directObject=combinations[directObject]
                    directObject=infinitive(current,inf,current[directObject])
                response=current.verb(subject,verb).ask(directObject)
                print(response)
                #talker.say(response)
                
            elif 'W' in links and 'i' in links['W']:
                #print "imperative sentece"
                subject="you"
                verbLink=links['W']
                verb=verbLink[verbLink.keys()[0]][0][1]
                directObject=None
                if any(tups[0]=='O' for tups in words[verb]):
                    objectLinks=filter(lambda tups:tups[0]=='O',words[verb])
                    directObject=links['O'][objectLinks[0][1]][0][1]
                elif any(tups[0]== 'P' for tups in words[verb]):
                    objectLinks=filter(lambda tups:tups[0]=='P',words[verb])
                    directObject=links['P'][objectLinks[0][1]][0][1]
                verb=combinations[verb]
                directObject=combinations[directObject]
                response=current.verb(subject,verb).act(current[directObject])
                print(response)
                #talker.say(response)
                
            elif 'W' in links and 'd' in links['W']:
                #print "declarative sentence"
                if 'S' in links:
                    SV=links['S']
                elif 'SX' in links:
                    SV=links['SX']
                subject=SV[list(SV.keys())[0]][0][0]
                verb=SV[list(SV.keys())[0]][0][1]
                verbLinks=words[verb]
                subject=combinations[subject]
                verb=combinations[verb]
                adv=None
                if any(tups[0]=='N' for tups in verbLinks):
                    advLinks=filter(lambda tups:tups[0]=='N',verbLinks)
                    adv=links['N'][advLinks[0][1]][0][1]
                    adv=combinations[adv]
                    adv=adverb(stripSub(adv),current)
                if any(tups[0]=='EB' for tups in verbLinks):
                    advLinks=filter(lambda tups:tups[0]=='EB',verbLinks)
                    adv=links['EB'][advLinks[0][1]][0][1]
                    adv=combinations[adv]
                    adv=adverb(stripSub(adv),current)
                directObject=None
                if any(tups[0]=='O' for tups in verbLinks):
                    objectLinks=[tups for tups in verbLinks if tups[0]=='O']
                    directObject=links['O'][objectLinks[0][1]][0][1]
                    directObject=combinations[directObject]
                    directObject=current[directObject]
                elif any(tups[0]== 'P' for tups in verbLinks):
                    objectLinks=filter(lambda tups:tups[0]=='P',verbLinks)
                    directObject=links['P'][objectLinks[0][1]][0][1]
                    directObject=combinations[directObject]
                    directObject=current[directObject]
                elif any(tups[0]=='I' for tups in verbLinks):
                    inf=links['I'][filter(lambda tups:tups[0]=='I',verbLinks)[0][1]][0][1]
                    infLinks=words[inf]
                    inf=combinations[inf]
                    if any(tups[0]=='O' for tups in infLinks):
                        directObject=links['O'][filter(lambda tups:tups[0]=='O',infLinks)[0][1]][0][1]
##                    elif any(tups[0]=='B' for tups in infLinks):
##                        directObject=links['B'][filter(lambda tups:tups[0]=='B',infLinks)[0][1]][0][0]
                    directObject=combinations[directObject]
                    directObject=infinitive(current,inf,current[directObject])
                current.verb(subject,verb)(directObject,adv=adv)
        except KeyError as value:   #conjugate 'be' for argmuent
            response="What is "+stripSub(value.args[0])+"?"
            print(response)
            #talker.say(response)
            raise
        except AttributeError as value:
            print(str(value.args[0]))
            #talker.say(str(value.args[0]))
            raise
    #hereafter are gramatically incorect commands
    elif 'run' in words:
        print(words)
    elif 'exit' in words:
        print(words)
    else:
        print("My responses are limited. Please use precise English")

# For now explicitly delete sentence
del linkage
del sent
