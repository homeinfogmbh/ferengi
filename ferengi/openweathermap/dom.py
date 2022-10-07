# ./ferengi/openweathermap/dom.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:cdb3cd4f2ddceef8f5df97096069e4c798ea713e
# Generated 2022-10-07 14:32:36.140076 by PyXB version 1.2.7-DEV using Python 3.10.7.final.0
# Namespace http://xml.homeinfo.de/schema/ferengi/weather

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1fa1631a-463c-11ed-a25f-7427eaa9df7d')

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
Namespace = pyxb.namespace.NamespaceForURI('http://xml.homeinfo.de/schema/ferengi/weather', create_if_missing=True)
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


# Complex type {http://xml.homeinfo.de/schema/ferengi/weather}Weather with content type ELEMENT_ONLY
class Weather (pyxb.binding.basis.complexTypeDefinition):
    """
                Wetterinformationen.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Weather')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 22, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element pubdate uses Python identifier pubdate
    __pubdate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'pubdate'), 'pubdate', '__httpxml_homeinfo_deschemaferengiweather_Weather_pubdate', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 29, 12), )

    
    pubdate = property(__pubdate.value, __pubdate.set, None, '\n                        Datum der veröffentlichung.\n                    ')

    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpxml_homeinfo_deschemaferengiweather_Weather_name', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 36, 12), )

    
    name = property(__name.value, __name.set, None, '\n                        Name des Ortes.\n                    ')

    
    # Element forecast uses Python identifier forecast
    __forecast = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'forecast'), 'forecast', '__httpxml_homeinfo_deschemaferengiweather_Weather_forecast', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 43, 12), )

    
    forecast = property(__forecast.value, __forecast.set, None, '\n                        Die Wettervorhersage.\n                    ')

    _ElementMap.update({
        __pubdate.name() : __pubdate,
        __name.name() : __name,
        __forecast.name() : __forecast
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Weather = Weather
Namespace.addCategoryObject('typeBinding', 'Weather', Weather)


# Complex type {http://xml.homeinfo.de/schema/ferengi/weather}Forecast with content type ELEMENT_ONLY
class Forecast (pyxb.binding.basis.complexTypeDefinition):
    """
                Wettervorhersagen.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Forecast')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 54, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element day uses Python identifier day
    __day = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'day'), 'day', '__httpxml_homeinfo_deschemaferengiweather_Forecast_day', True, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 61, 12), )

    
    day = property(__day.value, __day.set, None, '\n                        Wettervorhersagen pro Tag.\n                    ')

    _ElementMap.update({
        __day.name() : __day
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.Forecast = Forecast
Namespace.addCategoryObject('typeBinding', 'Forecast', Forecast)


# Complex type {http://xml.homeinfo.de/schema/ferengi/weather}DayForecast with content type EMPTY
class DayForecast (pyxb.binding.basis.complexTypeDefinition):
    """
                Wettervorhersage für einen Tag.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DayForecast')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 72, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute icon_id uses Python identifier icon_id
    __icon_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'icon_id'), 'icon_id', '__httpxml_homeinfo_deschemaferengiweather_DayForecast_icon_id', pyxb.binding.datatypes.integer)
    __icon_id._DeclarationLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 78, 8)
    __icon_id._UseLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 78, 8)
    
    icon_id = property(__icon_id.value, __icon_id.set, None, '\n                    Wetter Icon.\n                ')

    
    # Attribute weather_text uses Python identifier weather_text
    __weather_text = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'weather_text'), 'weather_text', '__httpxml_homeinfo_deschemaferengiweather_DayForecast_weather_text', pyxb.binding.datatypes.string)
    __weather_text._DeclarationLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 85, 8)
    __weather_text._UseLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 85, 8)
    
    weather_text = property(__weather_text.value, __weather_text.set, None, '\n                    Wetterbeschreibung.\n                ')

    
    # Attribute tempmin uses Python identifier tempmin
    __tempmin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tempmin'), 'tempmin', '__httpxml_homeinfo_deschemaferengiweather_DayForecast_tempmin', pyxb.binding.datatypes.integer)
    __tempmin._DeclarationLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 92, 8)
    __tempmin._UseLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 92, 8)
    
    tempmin = property(__tempmin.value, __tempmin.set, None, '\n                    Minimale Temperatur.\n                ')

    
    # Attribute tempmax uses Python identifier tempmax
    __tempmax = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tempmax'), 'tempmax', '__httpxml_homeinfo_deschemaferengiweather_DayForecast_tempmax', pyxb.binding.datatypes.integer)
    __tempmax._DeclarationLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 99, 8)
    __tempmax._UseLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 99, 8)
    
    tempmax = property(__tempmax.value, __tempmax.set, None, '\n                    Maximale Temperatur.\n                ')

    
    # Attribute date uses Python identifier date
    __date = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'date'), 'date', '__httpxml_homeinfo_deschemaferengiweather_DayForecast_date', pyxb.binding.datatypes.date)
    __date._DeclarationLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 106, 8)
    __date._UseLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 106, 8)
    
    date = property(__date.value, __date.set, None, '\n                    Datum der Wettervorhersage.\n                ')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __icon_id.name() : __icon_id,
        __weather_text.name() : __weather_text,
        __tempmin.name() : __tempmin,
        __tempmax.name() : __tempmax,
        __date.name() : __date
    })
_module_typeBindings.DayForecast = DayForecast
Namespace.addCategoryObject('typeBinding', 'DayForecast', DayForecast)


xml = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xml'), Weather, documentation='\n                Wurzelelement.\n            ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 13, 4))
Namespace.addCategoryObject('elementBinding', xml.name().localName(), xml)



Weather._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'pubdate'), pyxb.binding.datatypes.string, scope=Weather, documentation='\n                        Datum der veröffentlichung.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 29, 12)))

Weather._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=Weather, documentation='\n                        Name des Ortes.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 36, 12)))

Weather._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'forecast'), Forecast, scope=Weather, documentation='\n                        Die Wettervorhersage.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 43, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Weather._UseForTag(pyxb.namespace.ExpandedName(None, 'pubdate')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 29, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(Weather._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 36, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Weather._UseForTag(pyxb.namespace.ExpandedName(None, 'forecast')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 43, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Weather._Automaton = _BuildAutomaton()




Forecast._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'day'), DayForecast, scope=Forecast, documentation='\n                        Wettervorhersagen pro Tag.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 61, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(Forecast._UseForTag(pyxb.namespace.ExpandedName(None, 'day')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/weather.xsd', 61, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
Forecast._Automaton = _BuildAutomaton_()

