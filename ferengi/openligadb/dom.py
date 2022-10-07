# ./ferengi/openligadb/dom.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:091018c179afb95c1cc3b304ba655ce27bdb3cc5
# Generated 2022-10-07 14:32:35.871650 by PyXB version 1.2.7-DEV using Python 3.10.7.final.0
# Namespace http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:1f73a0ba-463c-11ed-84b1-7427eaa9df7d')

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
Namespace = pyxb.namespace.NamespaceForURI('http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api', create_if_missing=True)
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


# Complex type {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}ArrayOfBlTableTeamType with content type ELEMENT_ONLY
class ArrayOfBlTableTeamType (pyxb.binding.basis.complexTypeDefinition):
    """
                Liste von Mannschaften in der Tabelle.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArrayOfBlTableTeamType')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 23, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}BlTableTeam uses Python identifier BlTableTeam
    __BlTableTeam = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BlTableTeam'), 'BlTableTeam', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_ArrayOfBlTableTeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiBlTableTeam', True, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 30, 12), )

    
    BlTableTeam = property(__BlTableTeam.value, __BlTableTeam.set, None, '\n                        Einzelne Spiele.\n                    ')

    _ElementMap.update({
        __BlTableTeam.name() : __BlTableTeam
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ArrayOfBlTableTeamType = ArrayOfBlTableTeamType
Namespace.addCategoryObject('typeBinding', 'ArrayOfBlTableTeamType', ArrayOfBlTableTeamType)


# Complex type {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}BlTableTeamType with content type ELEMENT_ONLY
class BlTableTeamType (pyxb.binding.basis.complexTypeDefinition):
    """
                Mannschaftsinformation für die Tabelle.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BlTableTeamType')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 41, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}Draw uses Python identifier Draw
    __Draw = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Draw'), 'Draw', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_BlTableTeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiDraw', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 48, 12), )

    
    Draw = property(__Draw.value, __Draw.set, None, '\n                        Anzahl Unentschieden.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}Goals uses Python identifier Goals
    __Goals = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Goals'), 'Goals', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_BlTableTeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiGoals', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 55, 12), )

    
    Goals = property(__Goals.value, __Goals.set, None, '\n                        Anzahl Tore.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}Lost uses Python identifier Lost
    __Lost = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Lost'), 'Lost', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_BlTableTeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiLost', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 62, 12), )

    
    Lost = property(__Lost.value, __Lost.set, None, '\n                        Anzahl Niederlagen.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}Matches uses Python identifier Matches
    __Matches = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Matches'), 'Matches', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_BlTableTeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiMatches', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 69, 12), )

    
    Matches = property(__Matches.value, __Matches.set, None, '\n                        Anzahl Spiele.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}OpponentGoals uses Python identifier OpponentGoals
    __OpponentGoals = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OpponentGoals'), 'OpponentGoals', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_BlTableTeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiOpponentGoals', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 76, 12), )

    
    OpponentGoals = property(__OpponentGoals.value, __OpponentGoals.set, None, '\n                        Anzahl Gegentore.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}Points uses Python identifier Points
    __Points = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Points'), 'Points', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_BlTableTeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiPoints', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 83, 12), )

    
    Points = property(__Points.value, __Points.set, None, '\n                        Punkte.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}ShortName uses Python identifier ShortName
    __ShortName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ShortName'), 'ShortName', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_BlTableTeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiShortName', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 90, 12), )

    
    ShortName = property(__ShortName.value, __ShortName.set, None, '\n                        Kürzel des Mannschaftsnamens.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}TeamIconUrl uses Python identifier TeamIconUrl
    __TeamIconUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamIconUrl'), 'TeamIconUrl', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_BlTableTeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiTeamIconUrl', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 97, 12), )

    
    TeamIconUrl = property(__TeamIconUrl.value, __TeamIconUrl.set, None, '\n                        URL zum Teamlogo.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}TeamInfoId uses Python identifier TeamInfoId
    __TeamInfoId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamInfoId'), 'TeamInfoId', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_BlTableTeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiTeamInfoId', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 104, 12), )

    
    TeamInfoId = property(__TeamInfoId.value, __TeamInfoId.set, None, '\n                        ID der Mannschaftsinformation in der Tabelle.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}TeamName uses Python identifier TeamName
    __TeamName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamName'), 'TeamName', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_BlTableTeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiTeamName', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 111, 12), )

    
    TeamName = property(__TeamName.value, __TeamName.set, None, '\n                        Voller Name der Mannschaft.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}Won uses Python identifier Won
    __Won = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Won'), 'Won', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_BlTableTeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiWon', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 118, 12), )

    
    Won = property(__Won.value, __Won.set, None, '\n                        Anzahl Siege.\n                    ')

    _ElementMap.update({
        __Draw.name() : __Draw,
        __Goals.name() : __Goals,
        __Lost.name() : __Lost,
        __Matches.name() : __Matches,
        __OpponentGoals.name() : __OpponentGoals,
        __Points.name() : __Points,
        __ShortName.name() : __ShortName,
        __TeamIconUrl.name() : __TeamIconUrl,
        __TeamInfoId.name() : __TeamInfoId,
        __TeamName.name() : __TeamName,
        __Won.name() : __Won
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BlTableTeamType = BlTableTeamType
Namespace.addCategoryObject('typeBinding', 'BlTableTeamType', BlTableTeamType)


# Complex type {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}ArrayOfMatchType with content type ELEMENT_ONLY
class ArrayOfMatchType (pyxb.binding.basis.complexTypeDefinition):
    """
                Liste von Spielen.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ArrayOfMatchType')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfMatch.xsd', 24, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}Match uses Python identifier Match
    __Match = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Match'), 'Match', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_ArrayOfMatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiMatch', True, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfMatch.xsd', 31, 12), )

    
    Match = property(__Match.value, __Match.set, None, '\n                        Einzelne Spiele.\n                    ')

    _ElementMap.update({
        __Match.name() : __Match
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.ArrayOfMatchType = ArrayOfMatchType
Namespace.addCategoryObject('typeBinding', 'ArrayOfMatchType', ArrayOfMatchType)


# Complex type {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}MatchType with content type ELEMENT_ONLY
class MatchType (pyxb.binding.basis.complexTypeDefinition):
    """
                Ein Spiel.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MatchType')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 23, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}Goals uses Python identifier Goals
    __Goals = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Goals'), 'Goals', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiGoals', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 30, 12), )

    
    Goals = property(__Goals.value, __Goals.set, None, '\n                        Tore.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}Group uses Python identifier Group
    __Group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Group'), 'Group', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiGroup', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 37, 12), )

    
    Group = property(__Group.value, __Group.set, None, '\n                        Gruppe.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}LastUpdateDateTime uses Python identifier LastUpdateDateTime
    __LastUpdateDateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LastUpdateDateTime'), 'LastUpdateDateTime', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiLastUpdateDateTime', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 44, 12), )

    
    LastUpdateDateTime = property(__LastUpdateDateTime.value, __LastUpdateDateTime.set, None, '\n                        Datum und Uhrzeit der letzten Aktualisierung.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}LeagueId uses Python identifier LeagueId
    __LeagueId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LeagueId'), 'LeagueId', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiLeagueId', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 51, 12), )

    
    LeagueId = property(__LeagueId.value, __LeagueId.set, None, '\n                        ID der Liga.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}LeagueName uses Python identifier LeagueName
    __LeagueName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LeagueName'), 'LeagueName', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiLeagueName', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 58, 12), )

    
    LeagueName = property(__LeagueName.value, __LeagueName.set, None, '\n                        Name der Liga.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}Location uses Python identifier Location
    __Location = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Location'), 'Location', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiLocation', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 65, 12), )

    
    Location = property(__Location.value, __Location.set, None, '\n                        ID der Liga.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}MatchDateTime uses Python identifier MatchDateTime
    __MatchDateTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MatchDateTime'), 'MatchDateTime', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiMatchDateTime', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 72, 12), )

    
    MatchDateTime = property(__MatchDateTime.value, __MatchDateTime.set, None, '\n                        Datum und Uhrzeit des Spiels in Ortszeit.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}MatchDateTimeUTC uses Python identifier MatchDateTimeUTC
    __MatchDateTimeUTC = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MatchDateTimeUTC'), 'MatchDateTimeUTC', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiMatchDateTimeUTC', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 79, 12), )

    
    MatchDateTimeUTC = property(__MatchDateTimeUTC.value, __MatchDateTimeUTC.set, None, '\n                        Datum und Uhrzeit des Spiels in UTC.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}MatchID uses Python identifier MatchID
    __MatchID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MatchID'), 'MatchID', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiMatchID', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 86, 12), )

    
    MatchID = property(__MatchID.value, __MatchID.set, None, '\n                        ID des Spiels.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}MatchIsFinished uses Python identifier MatchIsFinished
    __MatchIsFinished = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MatchIsFinished'), 'MatchIsFinished', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiMatchIsFinished', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 93, 12), )

    
    MatchIsFinished = property(__MatchIsFinished.value, __MatchIsFinished.set, None, '\n                        Ist das Spiel beendet?\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}MatchResults uses Python identifier MatchResults
    __MatchResults = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MatchResults'), 'MatchResults', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiMatchResults', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 100, 12), )

    
    MatchResults = property(__MatchResults.value, __MatchResults.set, None, '\n                        Details zum Spielausgang.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}NumberOfViewers uses Python identifier NumberOfViewers
    __NumberOfViewers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NumberOfViewers'), 'NumberOfViewers', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiNumberOfViewers', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 107, 12), )

    
    NumberOfViewers = property(__NumberOfViewers.value, __NumberOfViewers.set, None, '\n                        Anzahl der Zuschauer.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}Team1 uses Python identifier Team1
    __Team1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Team1'), 'Team1', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiTeam1', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 114, 12), )

    
    Team1 = property(__Team1.value, __Team1.set, None, '\n                        Heimteam.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}Team2 uses Python identifier Team2
    __Team2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Team2'), 'Team2', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiTeam2', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 121, 12), )

    
    Team2 = property(__Team2.value, __Team2.set, None, '\n                        Gastteam.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}TimeZoneID uses Python identifier TimeZoneID
    __TimeZoneID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TimeZoneID'), 'TimeZoneID', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiTimeZoneID', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 128, 12), )

    
    TimeZoneID = property(__TimeZoneID.value, __TimeZoneID.set, None, '\n                        Name der Zeitzone.\n                    ')

    _ElementMap.update({
        __Goals.name() : __Goals,
        __Group.name() : __Group,
        __LastUpdateDateTime.name() : __LastUpdateDateTime,
        __LeagueId.name() : __LeagueId,
        __LeagueName.name() : __LeagueName,
        __Location.name() : __Location,
        __MatchDateTime.name() : __MatchDateTime,
        __MatchDateTimeUTC.name() : __MatchDateTimeUTC,
        __MatchID.name() : __MatchID,
        __MatchIsFinished.name() : __MatchIsFinished,
        __MatchResults.name() : __MatchResults,
        __NumberOfViewers.name() : __NumberOfViewers,
        __Team1.name() : __Team1,
        __Team2.name() : __Team2,
        __TimeZoneID.name() : __TimeZoneID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MatchType = MatchType
Namespace.addCategoryObject('typeBinding', 'MatchType', MatchType)


# Complex type {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}GoalsType with content type ELEMENT_ONLY
class GoalsType (pyxb.binding.basis.complexTypeDefinition):
    """
                Liste von Toren.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GoalsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 139, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}Goal uses Python identifier Goal
    __Goal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Goal'), 'Goal', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_GoalsType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiGoal', True, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 146, 12), )

    
    Goal = property(__Goal.value, __Goal.set, None, '\n                        Tore.\n                    ')

    _ElementMap.update({
        __Goal.name() : __Goal
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GoalsType = GoalsType
Namespace.addCategoryObject('typeBinding', 'GoalsType', GoalsType)


# Complex type {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}GoalType with content type ELEMENT_ONLY
class GoalType (pyxb.binding.basis.complexTypeDefinition):
    """
                Informationen zu einem Tor.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GoalType')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 157, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}Comment uses Python identifier Comment
    __Comment = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Comment'), 'Comment', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_GoalType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiComment', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 164, 12), )

    
    Comment = property(__Comment.value, __Comment.set, None, '\n                        Kommentar zum Tor.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}GoalGetterID uses Python identifier GoalGetterID
    __GoalGetterID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GoalGetterID'), 'GoalGetterID', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_GoalType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiGoalGetterID', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 171, 12), )

    
    GoalGetterID = property(__GoalGetterID.value, __GoalGetterID.set, None, '\n                        Spieler ID des Torschützen.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}GoalGetterName uses Python identifier GoalGetterName
    __GoalGetterName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GoalGetterName'), 'GoalGetterName', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_GoalType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiGoalGetterName', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 178, 12), )

    
    GoalGetterName = property(__GoalGetterName.value, __GoalGetterName.set, None, '\n                        Name des Torschützen.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}GoalID uses Python identifier GoalID
    __GoalID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GoalID'), 'GoalID', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_GoalType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiGoalID', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 185, 12), )

    
    GoalID = property(__GoalID.value, __GoalID.set, None, '\n                        ID des Tors.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}IsOvertime uses Python identifier IsOvertime
    __IsOvertime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IsOvertime'), 'IsOvertime', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_GoalType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiIsOvertime', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 192, 12), )

    
    IsOvertime = property(__IsOvertime.value, __IsOvertime.set, None, '\n                        Ist das Tor in der Nachspielzeit gefallen?\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}IsOwnGoal uses Python identifier IsOwnGoal
    __IsOwnGoal = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IsOwnGoal'), 'IsOwnGoal', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_GoalType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiIsOwnGoal', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 199, 12), )

    
    IsOwnGoal = property(__IsOwnGoal.value, __IsOwnGoal.set, None, '\n                        Handelt es sich um ein Eigentor?\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}IsPenalty uses Python identifier IsPenalty
    __IsPenalty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IsPenalty'), 'IsPenalty', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_GoalType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiIsPenalty', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 206, 12), )

    
    IsPenalty = property(__IsPenalty.value, __IsPenalty.set, None, '\n                        Ist das Tor im Rahmen eines Strafstoßes gefallen?\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}MatchMinute uses Python identifier MatchMinute
    __MatchMinute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MatchMinute'), 'MatchMinute', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_GoalType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiMatchMinute', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 213, 12), )

    
    MatchMinute = property(__MatchMinute.value, __MatchMinute.set, None, '\n                        Spielminute, in welcher das Tor gefallen ist.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}ScoreTeam1 uses Python identifier ScoreTeam1
    __ScoreTeam1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ScoreTeam1'), 'ScoreTeam1', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_GoalType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiScoreTeam1', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 220, 12), )

    
    ScoreTeam1 = property(__ScoreTeam1.value, __ScoreTeam1.set, None, '\n                        Torstand Heimteam.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}ScoreTeam2 uses Python identifier ScoreTeam2
    __ScoreTeam2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ScoreTeam2'), 'ScoreTeam2', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_GoalType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiScoreTeam2', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 227, 12), )

    
    ScoreTeam2 = property(__ScoreTeam2.value, __ScoreTeam2.set, None, '\n                        Torstand Gastteam.\n                    ')

    _ElementMap.update({
        __Comment.name() : __Comment,
        __GoalGetterID.name() : __GoalGetterID,
        __GoalGetterName.name() : __GoalGetterName,
        __GoalID.name() : __GoalID,
        __IsOvertime.name() : __IsOvertime,
        __IsOwnGoal.name() : __IsOwnGoal,
        __IsPenalty.name() : __IsPenalty,
        __MatchMinute.name() : __MatchMinute,
        __ScoreTeam1.name() : __ScoreTeam1,
        __ScoreTeam2.name() : __ScoreTeam2
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GoalType = GoalType
Namespace.addCategoryObject('typeBinding', 'GoalType', GoalType)


# Complex type {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}GroupType with content type ELEMENT_ONLY
class GroupType (pyxb.binding.basis.complexTypeDefinition):
    """
                Informationen zur Spielgruppe.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroupType')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 238, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}GroupID uses Python identifier GroupID
    __GroupID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GroupID'), 'GroupID', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_GroupType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiGroupID', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 245, 12), )

    
    GroupID = property(__GroupID.value, __GroupID.set, None, '\n                        ID der Gruppe.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}GroupName uses Python identifier GroupName
    __GroupName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GroupName'), 'GroupName', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_GroupType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiGroupName', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 252, 12), )

    
    GroupName = property(__GroupName.value, __GroupName.set, None, '\n                        Name der Gruppe.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}GroupOrderID uses Python identifier GroupOrderID
    __GroupOrderID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GroupOrderID'), 'GroupOrderID', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_GroupType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiGroupOrderID', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 259, 12), )

    
    GroupOrderID = property(__GroupOrderID.value, __GroupOrderID.set, None, '\n                        Sortierindex der Gruppe.\n                    ')

    _ElementMap.update({
        __GroupID.name() : __GroupID,
        __GroupName.name() : __GroupName,
        __GroupOrderID.name() : __GroupOrderID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.GroupType = GroupType
Namespace.addCategoryObject('typeBinding', 'GroupType', GroupType)


# Complex type {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}LocationType with content type ELEMENT_ONLY
class LocationType (pyxb.binding.basis.complexTypeDefinition):
    """
                Informationen zum Spielort.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LocationType')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 270, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}LocationCity uses Python identifier LocationCity
    __LocationCity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LocationCity'), 'LocationCity', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_LocationType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiLocationCity', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 277, 12), )

    
    LocationCity = property(__LocationCity.value, __LocationCity.set, None, '\n                        Name der Stadt.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}LocationID uses Python identifier LocationID
    __LocationID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LocationID'), 'LocationID', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_LocationType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiLocationID', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 284, 12), )

    
    LocationID = property(__LocationID.value, __LocationID.set, None, '\n                        ID des Spielorts.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}LocationStadium uses Python identifier LocationStadium
    __LocationStadium = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LocationStadium'), 'LocationStadium', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_LocationType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiLocationStadium', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 291, 12), )

    
    LocationStadium = property(__LocationStadium.value, __LocationStadium.set, None, '\n                        Name des Stadions.\n                    ')

    _ElementMap.update({
        __LocationCity.name() : __LocationCity,
        __LocationID.name() : __LocationID,
        __LocationStadium.name() : __LocationStadium
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LocationType = LocationType
Namespace.addCategoryObject('typeBinding', 'LocationType', LocationType)


# Complex type {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}MatchResultsType with content type ELEMENT_ONLY
class MatchResultsType (pyxb.binding.basis.complexTypeDefinition):
    """
                Spielausgänge und Zwischenstände.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MatchResultsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 302, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}MatchResult uses Python identifier MatchResult
    __MatchResult = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MatchResult'), 'MatchResult', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchResultsType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiMatchResult', True, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 309, 12), )

    
    MatchResult = property(__MatchResult.value, __MatchResult.set, None, '\n                        Ergebnistypen.\n                    ')

    _ElementMap.update({
        __MatchResult.name() : __MatchResult
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MatchResultsType = MatchResultsType
Namespace.addCategoryObject('typeBinding', 'MatchResultsType', MatchResultsType)


# Complex type {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}MatchResultType with content type ELEMENT_ONLY
class MatchResultType (pyxb.binding.basis.complexTypeDefinition):
    """
                Spielausgangs- und Zwischenstands-Informationen.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MatchResultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 320, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}PointsTeam1 uses Python identifier PointsTeam1
    __PointsTeam1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PointsTeam1'), 'PointsTeam1', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchResultType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiPointsTeam1', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 327, 12), )

    
    PointsTeam1 = property(__PointsTeam1.value, __PointsTeam1.set, None, '\n                        Punkte für Heimteam.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}PointsTeam2 uses Python identifier PointsTeam2
    __PointsTeam2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PointsTeam2'), 'PointsTeam2', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchResultType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiPointsTeam2', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 334, 12), )

    
    PointsTeam2 = property(__PointsTeam2.value, __PointsTeam2.set, None, '\n                        Punkte für Gastteam.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}ResultDescription uses Python identifier ResultDescription
    __ResultDescription = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResultDescription'), 'ResultDescription', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchResultType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiResultDescription', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 341, 12), )

    
    ResultDescription = property(__ResultDescription.value, __ResultDescription.set, None, '\n                        Textbeschreibung des Ergebnis.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}ResultID uses Python identifier ResultID
    __ResultID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResultID'), 'ResultID', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchResultType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiResultID', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 348, 12), )

    
    ResultID = property(__ResultID.value, __ResultID.set, None, '\n                        ID des Spienstands.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}ResultName uses Python identifier ResultName
    __ResultName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResultName'), 'ResultName', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchResultType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiResultName', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 355, 12), )

    
    ResultName = property(__ResultName.value, __ResultName.set, None, '\n                        Textbeschreibung des Spielstands.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}ResultOrderID uses Python identifier ResultOrderID
    __ResultOrderID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResultOrderID'), 'ResultOrderID', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchResultType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiResultOrderID', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 362, 12), )

    
    ResultOrderID = property(__ResultOrderID.value, __ResultOrderID.set, None, '\n                        Sortierindex.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}ResultTypeID uses Python identifier ResultTypeID
    __ResultTypeID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ResultTypeID'), 'ResultTypeID', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_MatchResultType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiResultTypeID', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 369, 12), )

    
    ResultTypeID = property(__ResultTypeID.value, __ResultTypeID.set, None, '\n                        Typ des Ergebnisses oder Zwischenstands.\n                    ')

    _ElementMap.update({
        __PointsTeam1.name() : __PointsTeam1,
        __PointsTeam2.name() : __PointsTeam2,
        __ResultDescription.name() : __ResultDescription,
        __ResultID.name() : __ResultID,
        __ResultName.name() : __ResultName,
        __ResultOrderID.name() : __ResultOrderID,
        __ResultTypeID.name() : __ResultTypeID
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.MatchResultType = MatchResultType
Namespace.addCategoryObject('typeBinding', 'MatchResultType', MatchResultType)


# Complex type {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}TeamType with content type ELEMENT_ONLY
class TeamType (pyxb.binding.basis.complexTypeDefinition):
    """
                Informationen zum einem Team.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TeamType')
    _XSDLocation = pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 380, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}ShortName uses Python identifier ShortName
    __ShortName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ShortName'), 'ShortName', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_TeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiShortName', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 387, 12), )

    
    ShortName = property(__ShortName.value, __ShortName.set, None, '\n                        Kürzel des Teams.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}TeamGroupName uses Python identifier TeamGroupName
    __TeamGroupName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamGroupName'), 'TeamGroupName', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_TeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiTeamGroupName', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 394, 12), )

    
    TeamGroupName = property(__TeamGroupName.value, __TeamGroupName.set, None, '\n                        Gruppenname des Teams. (?)\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}TeamIconUrl uses Python identifier TeamIconUrl
    __TeamIconUrl = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamIconUrl'), 'TeamIconUrl', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_TeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiTeamIconUrl', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 401, 12), )

    
    TeamIconUrl = property(__TeamIconUrl.value, __TeamIconUrl.set, None, '\n                        URL zum Teamlogo.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}TeamId uses Python identifier TeamId
    __TeamId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamId'), 'TeamId', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_TeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiTeamId', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 408, 12), )

    
    TeamId = property(__TeamId.value, __TeamId.set, None, '\n                        ID des Teams.\n                    ')

    
    # Element {http://schemas.datacontract.org/2004/07/OLDB.Spa.Models.Api}TeamName uses Python identifier TeamName
    __TeamName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'TeamName'), 'TeamName', '__httpschemas_datacontract_org200407OLDB_Spa_Models_Api_TeamType_httpschemas_datacontract_org200407OLDB_Spa_Models_ApiTeamName', False, pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 415, 12), )

    
    TeamName = property(__TeamName.value, __TeamName.set, None, '\n                        Voller Name des Teams.\n                    ')

    _ElementMap.update({
        __ShortName.name() : __ShortName,
        __TeamGroupName.name() : __TeamGroupName,
        __TeamIconUrl.name() : __TeamIconUrl,
        __TeamId.name() : __TeamId,
        __TeamName.name() : __TeamName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.TeamType = TeamType
Namespace.addCategoryObject('typeBinding', 'TeamType', TeamType)


ArrayOfBlTableTeam = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ArrayOfBlTableTeam'), ArrayOfBlTableTeamType, documentation='\n                Wurzelelement.\n            ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 14, 4))
Namespace.addCategoryObject('elementBinding', ArrayOfBlTableTeam.name().localName(), ArrayOfBlTableTeam)

ArrayOfMatch = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ArrayOfMatch'), ArrayOfMatchType, documentation='\n                Wurzelelement.\n            ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfMatch.xsd', 15, 4))
Namespace.addCategoryObject('elementBinding', ArrayOfMatch.name().localName(), ArrayOfMatch)

Match = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Match'), MatchType, documentation='\n                Wurzelelement.\n            ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 14, 4))
Namespace.addCategoryObject('elementBinding', Match.name().localName(), Match)



ArrayOfBlTableTeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BlTableTeam'), BlTableTeamType, scope=ArrayOfBlTableTeamType, documentation='\n                        Einzelne Spiele.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 30, 12)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 30, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ArrayOfBlTableTeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BlTableTeam')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 30, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ArrayOfBlTableTeamType._Automaton = _BuildAutomaton()




BlTableTeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Draw'), pyxb.binding.datatypes.unsignedByte, scope=BlTableTeamType, documentation='\n                        Anzahl Unentschieden.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 48, 12)))

BlTableTeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Goals'), pyxb.binding.datatypes.unsignedShort, scope=BlTableTeamType, documentation='\n                        Anzahl Tore.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 55, 12)))

BlTableTeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Lost'), pyxb.binding.datatypes.unsignedByte, scope=BlTableTeamType, documentation='\n                        Anzahl Niederlagen.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 62, 12)))

BlTableTeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Matches'), pyxb.binding.datatypes.unsignedByte, scope=BlTableTeamType, documentation='\n                        Anzahl Spiele.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 69, 12)))

BlTableTeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OpponentGoals'), pyxb.binding.datatypes.unsignedByte, scope=BlTableTeamType, documentation='\n                        Anzahl Gegentore.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 76, 12)))

BlTableTeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Points'), pyxb.binding.datatypes.unsignedByte, scope=BlTableTeamType, documentation='\n                        Punkte.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 83, 12)))

BlTableTeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShortName'), pyxb.binding.datatypes.string, scope=BlTableTeamType, documentation='\n                        Kürzel des Mannschaftsnamens.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 90, 12)))

BlTableTeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamIconUrl'), pyxb.binding.datatypes.string, scope=BlTableTeamType, documentation='\n                        URL zum Teamlogo.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 97, 12)))

BlTableTeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamInfoId'), pyxb.binding.datatypes.unsignedInt, scope=BlTableTeamType, documentation='\n                        ID der Mannschaftsinformation in der Tabelle.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 104, 12)))

BlTableTeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamName'), pyxb.binding.datatypes.string, scope=BlTableTeamType, documentation='\n                        Voller Name der Mannschaft.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 111, 12)))

BlTableTeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Won'), pyxb.binding.datatypes.unsignedByte, scope=BlTableTeamType, documentation='\n                        Anzahl Siege.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 118, 12)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BlTableTeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Draw')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 48, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BlTableTeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Goals')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 55, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BlTableTeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Lost')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 62, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BlTableTeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Matches')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 69, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BlTableTeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OpponentGoals')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 76, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BlTableTeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Points')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 83, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BlTableTeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ShortName')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 90, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BlTableTeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamIconUrl')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 97, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BlTableTeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamInfoId')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 104, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(BlTableTeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamName')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 111, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(BlTableTeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Won')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfBlTableTeam.xsd', 118, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
BlTableTeamType._Automaton = _BuildAutomaton_()




ArrayOfMatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Match'), MatchType, scope=ArrayOfMatchType, documentation='\n                        Einzelne Spiele.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfMatch.xsd', 31, 12)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfMatch.xsd', 31, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ArrayOfMatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Match')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/ArrayOfMatch.xsd', 31, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ArrayOfMatchType._Automaton = _BuildAutomaton_2()




MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Goals'), GoalsType, scope=MatchType, documentation='\n                        Tore.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 30, 12)))

MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Group'), GroupType, scope=MatchType, documentation='\n                        Gruppe.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 37, 12)))

MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LastUpdateDateTime'), pyxb.binding.datatypes.dateTime, scope=MatchType, documentation='\n                        Datum und Uhrzeit der letzten Aktualisierung.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 44, 12)))

MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LeagueId'), pyxb.binding.datatypes.unsignedInt, scope=MatchType, documentation='\n                        ID der Liga.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 51, 12)))

MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LeagueName'), pyxb.binding.datatypes.string, scope=MatchType, documentation='\n                        Name der Liga.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 58, 12)))

MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Location'), LocationType, nillable=pyxb.binding.datatypes.boolean(1), scope=MatchType, documentation='\n                        ID der Liga.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 65, 12)))

MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MatchDateTime'), pyxb.binding.datatypes.dateTime, scope=MatchType, documentation='\n                        Datum und Uhrzeit des Spiels in Ortszeit.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 72, 12)))

MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MatchDateTimeUTC'), pyxb.binding.datatypes.dateTime, scope=MatchType, documentation='\n                        Datum und Uhrzeit des Spiels in UTC.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 79, 12)))

MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MatchID'), pyxb.binding.datatypes.unsignedInt, scope=MatchType, documentation='\n                        ID des Spiels.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 86, 12)))

MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MatchIsFinished'), pyxb.binding.datatypes.boolean, scope=MatchType, documentation='\n                        Ist das Spiel beendet?\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 93, 12)))

MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MatchResults'), MatchResultsType, scope=MatchType, documentation='\n                        Details zum Spielausgang.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 100, 12)))

MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NumberOfViewers'), pyxb.binding.datatypes.unsignedInt, nillable=pyxb.binding.datatypes.boolean(1), scope=MatchType, documentation='\n                        Anzahl der Zuschauer.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 107, 12)))

MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Team1'), TeamType, scope=MatchType, documentation='\n                        Heimteam.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 114, 12)))

MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Team2'), TeamType, scope=MatchType, documentation='\n                        Gastteam.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 121, 12)))

MatchType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TimeZoneID'), pyxb.binding.datatypes.string, scope=MatchType, documentation='\n                        Name der Zeitzone.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 128, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Goals')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 30, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Group')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 37, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LastUpdateDateTime')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 44, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LeagueId')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 51, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LeagueName')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 58, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Location')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 65, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MatchDateTime')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 72, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MatchDateTimeUTC')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 79, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MatchID')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 86, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MatchIsFinished')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 93, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MatchResults')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 100, 12))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NumberOfViewers')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 107, 12))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Team1')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 114, 12))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Team2')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 121, 12))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MatchType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TimeZoneID')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 128, 12))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
         ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MatchType._Automaton = _BuildAutomaton_3()




GoalsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Goal'), GoalType, scope=GoalsType, documentation='\n                        Tore.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 146, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 146, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GoalsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Goal')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 146, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GoalsType._Automaton = _BuildAutomaton_4()




GoalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Comment'), pyxb.binding.datatypes.string, scope=GoalType, documentation='\n                        Kommentar zum Tor.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 164, 12)))

GoalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GoalGetterID'), pyxb.binding.datatypes.unsignedInt, scope=GoalType, documentation='\n                        Spieler ID des Torschützen.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 171, 12)))

GoalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GoalGetterName'), pyxb.binding.datatypes.string, scope=GoalType, documentation='\n                        Name des Torschützen.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 178, 12)))

GoalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GoalID'), pyxb.binding.datatypes.unsignedInt, scope=GoalType, documentation='\n                        ID des Tors.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 185, 12)))

GoalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IsOvertime'), pyxb.binding.datatypes.boolean, scope=GoalType, documentation='\n                        Ist das Tor in der Nachspielzeit gefallen?\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 192, 12)))

GoalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IsOwnGoal'), pyxb.binding.datatypes.boolean, scope=GoalType, documentation='\n                        Handelt es sich um ein Eigentor?\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 199, 12)))

GoalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IsPenalty'), pyxb.binding.datatypes.boolean, scope=GoalType, documentation='\n                        Ist das Tor im Rahmen eines Strafstoßes gefallen?\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 206, 12)))

GoalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MatchMinute'), pyxb.binding.datatypes.unsignedByte, scope=GoalType, documentation='\n                        Spielminute, in welcher das Tor gefallen ist.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 213, 12)))

GoalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ScoreTeam1'), pyxb.binding.datatypes.unsignedByte, scope=GoalType, documentation='\n                        Torstand Heimteam.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 220, 12)))

GoalType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ScoreTeam2'), pyxb.binding.datatypes.unsignedByte, scope=GoalType, documentation='\n                        Torstand Gastteam.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 227, 12)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GoalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Comment')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 164, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GoalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GoalGetterID')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 171, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GoalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GoalGetterName')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 178, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GoalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GoalID')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 185, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GoalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IsOvertime')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 192, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GoalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IsOwnGoal')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 199, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GoalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IsPenalty')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 206, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GoalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MatchMinute')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 213, 12))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GoalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ScoreTeam1')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 220, 12))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GoalType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ScoreTeam2')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 227, 12))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GoalType._Automaton = _BuildAutomaton_5()




GroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GroupID'), pyxb.binding.datatypes.unsignedInt, scope=GroupType, documentation='\n                        ID der Gruppe.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 245, 12)))

GroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GroupName'), pyxb.binding.datatypes.string, scope=GroupType, documentation='\n                        Name der Gruppe.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 252, 12)))

GroupType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GroupOrderID'), pyxb.binding.datatypes.unsignedInt, scope=GroupType, documentation='\n                        Sortierindex der Gruppe.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 259, 12)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GroupID')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 245, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GroupName')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 252, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GroupType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GroupOrderID')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 259, 12))
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
GroupType._Automaton = _BuildAutomaton_6()




LocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LocationCity'), pyxb.binding.datatypes.string, scope=LocationType, documentation='\n                        Name der Stadt.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 277, 12)))

LocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LocationID'), pyxb.binding.datatypes.unsignedInt, scope=LocationType, documentation='\n                        ID des Spielorts.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 284, 12)))

LocationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LocationStadium'), pyxb.binding.datatypes.string, scope=LocationType, documentation='\n                        Name des Stadions.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 291, 12)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LocationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LocationCity')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 277, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LocationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LocationID')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 284, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LocationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LocationStadium')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 291, 12))
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
LocationType._Automaton = _BuildAutomaton_7()




MatchResultsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MatchResult'), MatchResultType, scope=MatchResultsType, documentation='\n                        Ergebnistypen.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 309, 12)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 309, 12))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MatchResultsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MatchResult')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 309, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MatchResultsType._Automaton = _BuildAutomaton_8()




MatchResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PointsTeam1'), pyxb.binding.datatypes.unsignedByte, scope=MatchResultType, documentation='\n                        Punkte für Heimteam.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 327, 12)))

MatchResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PointsTeam2'), pyxb.binding.datatypes.unsignedByte, scope=MatchResultType, documentation='\n                        Punkte für Gastteam.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 334, 12)))

MatchResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResultDescription'), pyxb.binding.datatypes.string, scope=MatchResultType, documentation='\n                        Textbeschreibung des Ergebnis.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 341, 12)))

MatchResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResultID'), pyxb.binding.datatypes.unsignedInt, scope=MatchResultType, documentation='\n                        ID des Spienstands.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 348, 12)))

MatchResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResultName'), pyxb.binding.datatypes.string, scope=MatchResultType, documentation='\n                        Textbeschreibung des Spielstands.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 355, 12)))

MatchResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResultOrderID'), pyxb.binding.datatypes.unsignedInt, scope=MatchResultType, documentation='\n                        Sortierindex.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 362, 12)))

MatchResultType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ResultTypeID'), pyxb.binding.datatypes.unsignedInt, scope=MatchResultType, documentation='\n                        Typ des Ergebnisses oder Zwischenstands.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 369, 12)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PointsTeam1')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 327, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PointsTeam2')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 334, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResultDescription')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 341, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResultID')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 348, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResultName')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 355, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MatchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResultOrderID')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 362, 12))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MatchResultType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ResultTypeID')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 369, 12))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MatchResultType._Automaton = _BuildAutomaton_9()




TeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ShortName'), pyxb.binding.datatypes.string, scope=TeamType, documentation='\n                        Kürzel des Teams.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 387, 12)))

TeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamGroupName'), pyxb.binding.datatypes.string, nillable=pyxb.binding.datatypes.boolean(1), scope=TeamType, documentation='\n                        Gruppenname des Teams. (?)\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 394, 12)))

TeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamIconUrl'), pyxb.binding.datatypes.string, scope=TeamType, documentation='\n                        URL zum Teamlogo.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 401, 12)))

TeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamId'), pyxb.binding.datatypes.unsignedInt, scope=TeamType, documentation='\n                        ID des Teams.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 408, 12)))

TeamType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TeamName'), pyxb.binding.datatypes.string, scope=TeamType, documentation='\n                        Voller Name des Teams.\n                    ', location=pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 415, 12)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ShortName')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 387, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamGroupName')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 394, 12))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamIconUrl')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 401, 12))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(TeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamId')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 408, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TeamType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'TeamName')), pyxb.utils.utility.Location('/home/neumann/Projekte/ferengi/xsds/openligadb/Match.xsd', 415, 12))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TeamType._Automaton = _BuildAutomaton_10()

