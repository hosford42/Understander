# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_clinkgrammar', [dirname(__file__)])
        except ImportError:
            import _clinkgrammar
            return _clinkgrammar
        if fp is not None:
            try:
                _mod = imp.load_module('_clinkgrammar', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _clinkgrammar = swig_import_helper()
    del swig_import_helper
else:
    import _clinkgrammar
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def new_stringray(*args):
  return _clinkgrammar.new_stringray(*args)
new_stringray = _clinkgrammar.new_stringray

def delete_stringray(*args):
  return _clinkgrammar.delete_stringray(*args)
delete_stringray = _clinkgrammar.delete_stringray

def stringray_getitem(*args):
  return _clinkgrammar.stringray_getitem(*args)
stringray_getitem = _clinkgrammar.stringray_getitem

def stringray_setitem(*args):
  return _clinkgrammar.stringray_setitem(*args)
stringray_setitem = _clinkgrammar.stringray_setitem

def linkgrammar_get_version():
  return _clinkgrammar.linkgrammar_get_version()
linkgrammar_get_version = _clinkgrammar.linkgrammar_get_version

def dictionary_create(*args):
  return _clinkgrammar.dictionary_create(*args)
dictionary_create = _clinkgrammar.dictionary_create

def dictionary_create_lang(*args):
  return _clinkgrammar.dictionary_create_lang(*args)
dictionary_create_lang = _clinkgrammar.dictionary_create_lang

def dictionary_create_default_lang():
  return _clinkgrammar.dictionary_create_default_lang()
dictionary_create_default_lang = _clinkgrammar.dictionary_create_default_lang

def dictionary_delete(*args):
  return _clinkgrammar.dictionary_delete(*args)
dictionary_delete = _clinkgrammar.dictionary_delete

def dictionary_get_max_cost(*args):
  return _clinkgrammar.dictionary_get_max_cost(*args)
dictionary_get_max_cost = _clinkgrammar.dictionary_get_max_cost

def dictionary_set_data_dir(*args):
  return _clinkgrammar.dictionary_set_data_dir(*args)
dictionary_set_data_dir = _clinkgrammar.dictionary_set_data_dir

def dictionary_get_data_dir():
  return _clinkgrammar.dictionary_get_data_dir()
dictionary_get_data_dir = _clinkgrammar.dictionary_get_data_dir

def dictionary_is_past_tense_form(*args):
  return _clinkgrammar.dictionary_is_past_tense_form(*args)
dictionary_is_past_tense_form = _clinkgrammar.dictionary_is_past_tense_form

def dictionary_is_entity(*args):
  return _clinkgrammar.dictionary_is_entity(*args)
dictionary_is_entity = _clinkgrammar.dictionary_is_entity

def parse_options_create():
  return _clinkgrammar.parse_options_create()
parse_options_create = _clinkgrammar.parse_options_create

def parse_options_delete(*args):
  return _clinkgrammar.parse_options_delete(*args)
parse_options_delete = _clinkgrammar.parse_options_delete

def parse_options_set_verbosity(*args):
  return _clinkgrammar.parse_options_set_verbosity(*args)
parse_options_set_verbosity = _clinkgrammar.parse_options_set_verbosity

def parse_options_get_verbosity(*args):
  return _clinkgrammar.parse_options_get_verbosity(*args)
parse_options_get_verbosity = _clinkgrammar.parse_options_get_verbosity

def parse_options_set_linkage_limit(*args):
  return _clinkgrammar.parse_options_set_linkage_limit(*args)
parse_options_set_linkage_limit = _clinkgrammar.parse_options_set_linkage_limit

def parse_options_get_linkage_limit(*args):
  return _clinkgrammar.parse_options_get_linkage_limit(*args)
parse_options_get_linkage_limit = _clinkgrammar.parse_options_get_linkage_limit

def parse_options_set_disjunct_cost(*args):
  return _clinkgrammar.parse_options_set_disjunct_cost(*args)
parse_options_set_disjunct_cost = _clinkgrammar.parse_options_set_disjunct_cost

def parse_options_get_disjunct_cost(*args):
  return _clinkgrammar.parse_options_get_disjunct_cost(*args)
parse_options_get_disjunct_cost = _clinkgrammar.parse_options_get_disjunct_cost

def parse_options_set_min_null_count(*args):
  return _clinkgrammar.parse_options_set_min_null_count(*args)
parse_options_set_min_null_count = _clinkgrammar.parse_options_set_min_null_count

def parse_options_get_min_null_count(*args):
  return _clinkgrammar.parse_options_get_min_null_count(*args)
parse_options_get_min_null_count = _clinkgrammar.parse_options_get_min_null_count

def parse_options_set_max_null_count(*args):
  return _clinkgrammar.parse_options_set_max_null_count(*args)
parse_options_set_max_null_count = _clinkgrammar.parse_options_set_max_null_count

def parse_options_get_max_null_count(*args):
  return _clinkgrammar.parse_options_get_max_null_count(*args)
parse_options_get_max_null_count = _clinkgrammar.parse_options_get_max_null_count

def parse_options_set_null_block(*args):
  return _clinkgrammar.parse_options_set_null_block(*args)
parse_options_set_null_block = _clinkgrammar.parse_options_set_null_block

def parse_options_get_null_block(*args):
  return _clinkgrammar.parse_options_get_null_block(*args)
parse_options_get_null_block = _clinkgrammar.parse_options_get_null_block

def parse_options_set_islands_ok(*args):
  return _clinkgrammar.parse_options_set_islands_ok(*args)
parse_options_set_islands_ok = _clinkgrammar.parse_options_set_islands_ok

def parse_options_get_islands_ok(*args):
  return _clinkgrammar.parse_options_get_islands_ok(*args)
parse_options_get_islands_ok = _clinkgrammar.parse_options_get_islands_ok

def parse_options_set_short_length(*args):
  return _clinkgrammar.parse_options_set_short_length(*args)
parse_options_set_short_length = _clinkgrammar.parse_options_set_short_length

def parse_options_get_short_length(*args):
  return _clinkgrammar.parse_options_get_short_length(*args)
parse_options_get_short_length = _clinkgrammar.parse_options_get_short_length

def parse_options_set_max_memory(*args):
  return _clinkgrammar.parse_options_set_max_memory(*args)
parse_options_set_max_memory = _clinkgrammar.parse_options_set_max_memory

def parse_options_get_max_memory(*args):
  return _clinkgrammar.parse_options_get_max_memory(*args)
parse_options_get_max_memory = _clinkgrammar.parse_options_get_max_memory

def parse_options_set_max_sentence_length(*args):
  return _clinkgrammar.parse_options_set_max_sentence_length(*args)
parse_options_set_max_sentence_length = _clinkgrammar.parse_options_set_max_sentence_length

def parse_options_get_max_sentence_length(*args):
  return _clinkgrammar.parse_options_get_max_sentence_length(*args)
parse_options_get_max_sentence_length = _clinkgrammar.parse_options_get_max_sentence_length

def parse_options_set_max_parse_time(*args):
  return _clinkgrammar.parse_options_set_max_parse_time(*args)
parse_options_set_max_parse_time = _clinkgrammar.parse_options_set_max_parse_time

def parse_options_get_max_parse_time(*args):
  return _clinkgrammar.parse_options_get_max_parse_time(*args)
parse_options_get_max_parse_time = _clinkgrammar.parse_options_get_max_parse_time

def parse_options_set_cost_model_type(*args):
  return _clinkgrammar.parse_options_set_cost_model_type(*args)
parse_options_set_cost_model_type = _clinkgrammar.parse_options_set_cost_model_type

def parse_options_get_cost_model_type(*args):
  return _clinkgrammar.parse_options_get_cost_model_type(*args)
parse_options_get_cost_model_type = _clinkgrammar.parse_options_get_cost_model_type

def parse_options_timer_expired(*args):
  return _clinkgrammar.parse_options_timer_expired(*args)
parse_options_timer_expired = _clinkgrammar.parse_options_timer_expired

def parse_options_memory_exhausted(*args):
  return _clinkgrammar.parse_options_memory_exhausted(*args)
parse_options_memory_exhausted = _clinkgrammar.parse_options_memory_exhausted

def parse_options_resources_exhausted(*args):
  return _clinkgrammar.parse_options_resources_exhausted(*args)
parse_options_resources_exhausted = _clinkgrammar.parse_options_resources_exhausted

def parse_options_set_screen_width(*args):
  return _clinkgrammar.parse_options_set_screen_width(*args)
parse_options_set_screen_width = _clinkgrammar.parse_options_set_screen_width

def parse_options_get_screen_width(*args):
  return _clinkgrammar.parse_options_get_screen_width(*args)
parse_options_get_screen_width = _clinkgrammar.parse_options_get_screen_width

def parse_options_set_allow_null(*args):
  return _clinkgrammar.parse_options_set_allow_null(*args)
parse_options_set_allow_null = _clinkgrammar.parse_options_set_allow_null

def parse_options_get_allow_null(*args):
  return _clinkgrammar.parse_options_get_allow_null(*args)
parse_options_get_allow_null = _clinkgrammar.parse_options_get_allow_null

def parse_options_set_display_walls(*args):
  return _clinkgrammar.parse_options_set_display_walls(*args)
parse_options_set_display_walls = _clinkgrammar.parse_options_set_display_walls

def parse_options_get_display_walls(*args):
  return _clinkgrammar.parse_options_get_display_walls(*args)
parse_options_get_display_walls = _clinkgrammar.parse_options_get_display_walls

def parse_options_set_all_short_connectors(*args):
  return _clinkgrammar.parse_options_set_all_short_connectors(*args)
parse_options_set_all_short_connectors = _clinkgrammar.parse_options_set_all_short_connectors

def parse_options_get_all_short_connectors(*args):
  return _clinkgrammar.parse_options_get_all_short_connectors(*args)
parse_options_get_all_short_connectors = _clinkgrammar.parse_options_get_all_short_connectors

def parse_options_reset_resources(*args):
  return _clinkgrammar.parse_options_reset_resources(*args)
parse_options_reset_resources = _clinkgrammar.parse_options_reset_resources

def sentence_create(*args):
  return _clinkgrammar.sentence_create(*args)
sentence_create = _clinkgrammar.sentence_create

def sentence_delete(*args):
  return _clinkgrammar.sentence_delete(*args)
sentence_delete = _clinkgrammar.sentence_delete

def sentence_parse(*args):
  return _clinkgrammar.sentence_parse(*args)
sentence_parse = _clinkgrammar.sentence_parse

def sentence_length(*args):
  return _clinkgrammar.sentence_length(*args)
sentence_length = _clinkgrammar.sentence_length

def sentence_get_word(*args):
  return _clinkgrammar.sentence_get_word(*args)
sentence_get_word = _clinkgrammar.sentence_get_word

def sentence_null_count(*args):
  return _clinkgrammar.sentence_null_count(*args)
sentence_null_count = _clinkgrammar.sentence_null_count

def sentence_num_linkages_found(*args):
  return _clinkgrammar.sentence_num_linkages_found(*args)
sentence_num_linkages_found = _clinkgrammar.sentence_num_linkages_found

def sentence_num_valid_linkages(*args):
  return _clinkgrammar.sentence_num_valid_linkages(*args)
sentence_num_valid_linkages = _clinkgrammar.sentence_num_valid_linkages

def sentence_num_linkages_post_processed(*args):
  return _clinkgrammar.sentence_num_linkages_post_processed(*args)
sentence_num_linkages_post_processed = _clinkgrammar.sentence_num_linkages_post_processed

def sentence_num_violations(*args):
  return _clinkgrammar.sentence_num_violations(*args)
sentence_num_violations = _clinkgrammar.sentence_num_violations

def sentence_and_cost(*args):
  return _clinkgrammar.sentence_and_cost(*args)
sentence_and_cost = _clinkgrammar.sentence_and_cost

def sentence_disjunct_cost(*args):
  return _clinkgrammar.sentence_disjunct_cost(*args)
sentence_disjunct_cost = _clinkgrammar.sentence_disjunct_cost

def sentence_link_cost(*args):
  return _clinkgrammar.sentence_link_cost(*args)
sentence_link_cost = _clinkgrammar.sentence_link_cost

def sentence_get_nth_word(*args):
  return _clinkgrammar.sentence_get_nth_word(*args)
sentence_get_nth_word = _clinkgrammar.sentence_get_nth_word

def sentence_nth_word_has_disjunction(*args):
  return _clinkgrammar.sentence_nth_word_has_disjunction(*args)
sentence_nth_word_has_disjunction = _clinkgrammar.sentence_nth_word_has_disjunction

def linkage_create(*args):
  return _clinkgrammar.linkage_create(*args)
linkage_create = _clinkgrammar.linkage_create

def linkage_free_diagram(*args):
  return _clinkgrammar.linkage_free_diagram(*args)
linkage_free_diagram = _clinkgrammar.linkage_free_diagram

def linkage_delete(*args):
  return _clinkgrammar.linkage_delete(*args)
linkage_delete = _clinkgrammar.linkage_delete

def linkage_print_diagram(*args):
  return _clinkgrammar.linkage_print_diagram(*args)
linkage_print_diagram = _clinkgrammar.linkage_print_diagram

def linkage_get_current_sublinkage(*args):
  return _clinkgrammar.linkage_get_current_sublinkage(*args)
linkage_get_current_sublinkage = _clinkgrammar.linkage_get_current_sublinkage

def linkage_set_current_sublinkage(*args):
  return _clinkgrammar.linkage_set_current_sublinkage(*args)
linkage_set_current_sublinkage = _clinkgrammar.linkage_set_current_sublinkage

def linkage_get_sentence(*args):
  return _clinkgrammar.linkage_get_sentence(*args)
linkage_get_sentence = _clinkgrammar.linkage_get_sentence

def linkage_get_num_sublinkages(*args):
  return _clinkgrammar.linkage_get_num_sublinkages(*args)
linkage_get_num_sublinkages = _clinkgrammar.linkage_get_num_sublinkages

def linkage_get_num_words(*args):
  return _clinkgrammar.linkage_get_num_words(*args)
linkage_get_num_words = _clinkgrammar.linkage_get_num_words

def linkage_get_num_links(*args):
  return _clinkgrammar.linkage_get_num_links(*args)
linkage_get_num_links = _clinkgrammar.linkage_get_num_links

def linkage_get_link_lword(*args):
  return _clinkgrammar.linkage_get_link_lword(*args)
linkage_get_link_lword = _clinkgrammar.linkage_get_link_lword

def linkage_get_link_rword(*args):
  return _clinkgrammar.linkage_get_link_rword(*args)
linkage_get_link_rword = _clinkgrammar.linkage_get_link_rword

def linkage_get_link_length(*args):
  return _clinkgrammar.linkage_get_link_length(*args)
linkage_get_link_length = _clinkgrammar.linkage_get_link_length

def linkage_get_link_label(*args):
  return _clinkgrammar.linkage_get_link_label(*args)
linkage_get_link_label = _clinkgrammar.linkage_get_link_label

def linkage_get_link_llabel(*args):
  return _clinkgrammar.linkage_get_link_llabel(*args)
linkage_get_link_llabel = _clinkgrammar.linkage_get_link_llabel

def linkage_get_link_rlabel(*args):
  return _clinkgrammar.linkage_get_link_rlabel(*args)
linkage_get_link_rlabel = _clinkgrammar.linkage_get_link_rlabel

def linkage_get_link_num_domains(*args):
  return _clinkgrammar.linkage_get_link_num_domains(*args)
linkage_get_link_num_domains = _clinkgrammar.linkage_get_link_num_domains

def linkage_get_link_domain_names(*args):
  return _clinkgrammar.linkage_get_link_domain_names(*args)
linkage_get_link_domain_names = _clinkgrammar.linkage_get_link_domain_names

def linkage_get_words(*args):
  return _clinkgrammar.linkage_get_words(*args)
linkage_get_words = _clinkgrammar.linkage_get_words

def linkage_get_word(*args):
  return _clinkgrammar.linkage_get_word(*args)
linkage_get_word = _clinkgrammar.linkage_get_word

def linkage_print_links_and_domains(*args):
  return _clinkgrammar.linkage_print_links_and_domains(*args)
linkage_print_links_and_domains = _clinkgrammar.linkage_print_links_and_domains

def linkage_free_links_and_domains(*args):
  return _clinkgrammar.linkage_free_links_and_domains(*args)
linkage_free_links_and_domains = _clinkgrammar.linkage_free_links_and_domains

def linkage_print_senses(*args):
  return _clinkgrammar.linkage_print_senses(*args)
linkage_print_senses = _clinkgrammar.linkage_print_senses

def linkage_free_senses(*args):
  return _clinkgrammar.linkage_free_senses(*args)
linkage_free_senses = _clinkgrammar.linkage_free_senses

def linkage_print_constituent_tree(*args):
  return _clinkgrammar.linkage_print_constituent_tree(*args)
linkage_print_constituent_tree = _clinkgrammar.linkage_print_constituent_tree

def linkage_free_constituent_tree_str(*args):
  return _clinkgrammar.linkage_free_constituent_tree_str(*args)
linkage_free_constituent_tree_str = _clinkgrammar.linkage_free_constituent_tree_str

def linkage_print_postscript(*args):
  return _clinkgrammar.linkage_print_postscript(*args)
linkage_print_postscript = _clinkgrammar.linkage_print_postscript

def linkage_free_postscript(*args):
  return _clinkgrammar.linkage_free_postscript(*args)
linkage_free_postscript = _clinkgrammar.linkage_free_postscript

def linkage_compute_union(*args):
  return _clinkgrammar.linkage_compute_union(*args)
linkage_compute_union = _clinkgrammar.linkage_compute_union

def linkage_unused_word_cost(*args):
  return _clinkgrammar.linkage_unused_word_cost(*args)
linkage_unused_word_cost = _clinkgrammar.linkage_unused_word_cost

def linkage_disjunct_cost(*args):
  return _clinkgrammar.linkage_disjunct_cost(*args)
linkage_disjunct_cost = _clinkgrammar.linkage_disjunct_cost

def linkage_and_cost(*args):
  return _clinkgrammar.linkage_and_cost(*args)
linkage_and_cost = _clinkgrammar.linkage_and_cost

def linkage_link_cost(*args):
  return _clinkgrammar.linkage_link_cost(*args)
linkage_link_cost = _clinkgrammar.linkage_link_cost

def linkage_corpus_cost(*args):
  return _clinkgrammar.linkage_corpus_cost(*args)
linkage_corpus_cost = _clinkgrammar.linkage_corpus_cost

def linkage_is_canonical(*args):
  return _clinkgrammar.linkage_is_canonical(*args)
linkage_is_canonical = _clinkgrammar.linkage_is_canonical

def linkage_is_improper(*args):
  return _clinkgrammar.linkage_is_improper(*args)
linkage_is_improper = _clinkgrammar.linkage_is_improper

def linkage_has_inconsistent_domains(*args):
  return _clinkgrammar.linkage_has_inconsistent_domains(*args)
linkage_has_inconsistent_domains = _clinkgrammar.linkage_has_inconsistent_domains

def linkage_get_violation_name(*args):
  return _clinkgrammar.linkage_get_violation_name(*args)
linkage_get_violation_name = _clinkgrammar.linkage_get_violation_name

def post_process_open(*args):
  return _clinkgrammar.post_process_open(*args)
post_process_open = _clinkgrammar.post_process_open

def post_process_close(*args):
  return _clinkgrammar.post_process_close(*args)
post_process_close = _clinkgrammar.post_process_close

def linkage_post_process(*args):
  return _clinkgrammar.linkage_post_process(*args)
linkage_post_process = _clinkgrammar.linkage_post_process

def linkage_constituent_tree(*args):
  return _clinkgrammar.linkage_constituent_tree(*args)
linkage_constituent_tree = _clinkgrammar.linkage_constituent_tree

def linkage_free_constituent_tree(*args):
  return _clinkgrammar.linkage_free_constituent_tree(*args)
linkage_free_constituent_tree = _clinkgrammar.linkage_free_constituent_tree

def linkage_constituent_node_get_label(*args):
  return _clinkgrammar.linkage_constituent_node_get_label(*args)
linkage_constituent_node_get_label = _clinkgrammar.linkage_constituent_node_get_label

def linkage_constituent_node_get_child(*args):
  return _clinkgrammar.linkage_constituent_node_get_child(*args)
linkage_constituent_node_get_child = _clinkgrammar.linkage_constituent_node_get_child

def linkage_constituent_node_get_next(*args):
  return _clinkgrammar.linkage_constituent_node_get_next(*args)
linkage_constituent_node_get_next = _clinkgrammar.linkage_constituent_node_get_next

def linkage_constituent_node_get_start(*args):
  return _clinkgrammar.linkage_constituent_node_get_start(*args)
linkage_constituent_node_get_start = _clinkgrammar.linkage_constituent_node_get_start

def linkage_constituent_node_get_end(*args):
  return _clinkgrammar.linkage_constituent_node_get_end(*args)
linkage_constituent_node_get_end = _clinkgrammar.linkage_constituent_node_get_end


