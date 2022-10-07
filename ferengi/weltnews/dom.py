# ./ferengi/weltnews/dom.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2022-10-07 14:32:36.376674 by PyXB version 1.2.7-DEV using Python 3.10.7.final.0
# Namespace AbsentNamespace0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1fc5e212-463c-11ed-95d3-7427eaa9df7d')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.7-DEV'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, fallback_namespace=None, location_base=None, default_namespace=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword fallback_namespace An absent L{pyxb.Namespace} instance
    to use for unqualified names when there is no default namespace in
    scope.  If unspecified or C{None}, the namespace of the module
    containing this function will be used, if it is an absent
    namespace.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.

    @keyword default_namespace An alias for @c fallback_namespace used
    in PyXB 1.1.4 through 1.2.6.  It behaved like a default namespace
    only for absent namespaces.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=fallback_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, fallback_namespace=None, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if fallback_namespace is None:
        fallback_namespace = default_namespace
    if fallback_namespace is None:
        fallback_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, fallback_namespace)


# Complex type N24News with content type ELEMENT_ONLY
class N24News (pyxb.binding.basis.complexTypeDefinition):
    """
                Root-Element Typ.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'N24News')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 14, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element news uses Python identifier news
    __news = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'news'), 'news', '__AbsentNamespace0_N24News_news', True, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 21, 12), )

    
    news = property(__news.value, __news.set, None, '\n                        Nachrichten.\n                    ')

    _ElementMap.update({
        __news.name() : __news
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.N24News = N24News
Namespace.addCategoryObject('typeBinding', 'N24News', N24News)


# Complex type News with content type ELEMENT_ONLY
class News (pyxb.binding.basis.complexTypeDefinition):
    """
                Nachrichten Typ.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'News')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 32, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element subline uses Python identifier subline
    __subline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'subline'), 'subline', '__AbsentNamespace0_News_subline', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 39, 12), )

    
    subline = property(__subline.value, __subline.set, None, '\n                        Untertitel.\n                    ')

    
    # Element headline uses Python identifier headline
    __headline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'headline'), 'headline', '__AbsentNamespace0_News_headline', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 46, 12), )

    
    headline = property(__headline.value, __headline.set, None, '\n                        Titel.\n                    ')

    
    # Element source uses Python identifier source
    __source = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'source'), 'source', '__AbsentNamespace0_News_source', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 53, 12), )

    
    source = property(__source.value, __source.set, None, '\n                        Quellenangabe.\n                    ')

    
    # Element textmessage uses Python identifier textmessage
    __textmessage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'textmessage'), 'textmessage', '__AbsentNamespace0_News_textmessage', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 60, 12), )

    
    textmessage = property(__textmessage.value, __textmessage.set, None, '\n                        Nachrichtentext.\n                    ')

    
    # Element published uses Python identifier published
    __published = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'published'), 'published', '__AbsentNamespace0_News_published', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 67, 12), )

    
    published = property(__published.value, __published.set, None, '\n                        Angabe zur Veröffentlichung.\n                    ')

    
    # Element image uses Python identifier image
    __image = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'image'), 'image', '__AbsentNamespace0_News_image', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 74, 12), )

    
    image = property(__image.value, __image.set, None, '\n                        Titelbild.\n                    ')

    
    # Element thumb uses Python identifier thumb
    __thumb = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'thumb'), 'thumb', '__AbsentNamespace0_News_thumb', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 81, 12), )

    
    thumb = property(__thumb.value, __thumb.set, None, '\n                        Miniaturbild.\n                    ')

    
    # Element video uses Python identifier video
    __video = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'video'), 'video', '__AbsentNamespace0_News_video', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 88, 12), )

    
    video = property(__video.value, __video.set, None, '\n                        Video.\n                    ')

    
    # Element webUrl uses Python identifier webUrl
    __webUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'webUrl'), 'webUrl', '__AbsentNamespace0_News_webUrl', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 95, 12), )

    
    webUrl = property(__webUrl.value, __webUrl.set, None, '\n                        Link zum Onlineartikel.\n                    ')

    _ElementMap.update({
        __subline.name() : __subline,
        __headline.name() : __headline,
        __source.name() : __source,
        __textmessage.name() : __textmessage,
        __published.name() : __published,
        __image.name() : __image,
        __thumb.name() : __thumb,
        __video.name() : __video,
        __webUrl.name() : __webUrl
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.News = News
Namespace.addCategoryObject('typeBinding', 'News', News)


# Complex type TypedString with content type SIMPLE
class TypedString (pyxb.binding.basis.complexTypeDefinition):
    """
                Zeichenkette mit Attribut "type".
            """
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TypedString')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 106, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'type'), 'type', '__AbsentNamespace0_TypedString_type', pyxb.binding.datatypes.string, required=True)
    __type._DeclarationLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 114, 16)
    __type._UseLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 114, 16)
    
    type = property(__type.value, __type.set, None, '\n                            Typ der Information.\n                        ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __type.name() : __type
    })
_module_typeBindings.TypedString = TypedString
Namespace.addCategoryObject('typeBinding', 'TypedString', TypedString)


n24news = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'n24news'), N24News, location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 12, 4))
Namespace.addCategoryObject('elementBinding', n24news.name().localName(), n24news)



N24News._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'news'), News, scope=N24News, documentation='\n                        Nachrichten.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 21, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 21, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(N24News._UseForTag(pyxb.namespace.ExpandedName(None, 'news')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 21, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
N24News._Automaton = _BuildAutomaton()




News._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'subline'), pyxb.binding.datatypes.string, scope=News, documentation='\n                        Untertitel.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 39, 12)))

News._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'headline'), pyxb.binding.datatypes.string, scope=News, documentation='\n                        Titel.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 46, 12)))

News._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'source'), pyxb.binding.datatypes.string, scope=News, documentation='\n                        Quellenangabe.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 53, 12)))

News._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'textmessage'), pyxb.binding.datatypes.string, scope=News, documentation='\n                        Nachrichtentext.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 60, 12)))

News._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'published'), TypedString, scope=News, documentation='\n                        Angabe zur Veröffentlichung.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 67, 12)))

News._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'image'), TypedString, scope=News, documentation='\n                        Titelbild.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 74, 12)))

News._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'thumb'), TypedString, scope=News, documentation='\n                        Miniaturbild.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 81, 12)))

News._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'video'), TypedString, scope=News, documentation='\n                        Video.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 88, 12)))

News._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'webUrl'), pyxb.binding.datatypes.string, scope=News, documentation='\n                        Link zum Onlineartikel.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 95, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 74, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 81, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 88, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 95, 12))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(News._UseForTag(pyxb.namespace.ExpandedName(None, 'subline')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 39, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(News._UseForTag(pyxb.namespace.ExpandedName(None, 'headline')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 46, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(News._UseForTag(pyxb.namespace.ExpandedName(None, 'source')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 53, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(News._UseForTag(pyxb.namespace.ExpandedName(None, 'textmessage')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 60, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(News._UseForTag(pyxb.namespace.ExpandedName(None, 'published')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 67, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(News._UseForTag(pyxb.namespace.ExpandedName(None, 'image')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 74, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(News._UseForTag(pyxb.namespace.ExpandedName(None, 'thumb')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 81, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(News._UseForTag(pyxb.namespace.ExpandedName(None, 'video')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 88, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(News._UseForTag(pyxb.namespace.ExpandedName(None, 'webUrl')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/welt.xsd', 95, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
News._Automaton = _BuildAutomaton_()

