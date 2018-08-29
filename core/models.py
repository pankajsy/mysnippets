from __future__ import unicode_literals
from account.models import Basemodel
from django.contrib.gis.db import models

CATEGORY = ( ("business","business"),
             ("entertainment" ,"entertainment"),
             ("general","general"),
             ("health","health"),
             ("science","science"),
             ("sports","sports"),
             ("technology","technology"),
            ("more","more"),
            )

TYPE = (
    ("class", "class"),
    ("function", "function"),
)

LANGUAGES = (('A#_.NET', 'A#_.NET'),
 ('A#_(Axiom)', 'A#_(Axiom)'),
 ('A-0_System', 'A-0_System'),
 ('A+', 'A+'),
 ('A++', 'A++'),
 ('ABAP', 'ABAP'),
 ('ABC', 'ABC'),
 ('ABC_ALGOL', 'ABC_ALGOL'),
 ('ABLE', 'ABLE'),
 ('ABSET', 'ABSET'),
 ('ABSYS', 'ABSYS'),
 ('ACC', 'ACC'),
 ('Accent', 'Accent'),
 ('Ace_DASL', 'Ace_DASL'),
 ('ACL2', 'ACL2'),
 ('ACT-III', 'ACT-III'),
 ('Action!', 'Action!'),
 ('ActionScript', 'ActionScript'),
 ('Ada', 'Ada'),
 ('Adenine', 'Adenine'),
 ('Agda', 'Agda'),
 ('Agilent_VEE', 'Agilent_VEE'),
 ('Agora', 'Agora'),
 ('AIMMS', 'AIMMS'),
 ('Alef', 'Alef'),
 ('ALF', 'ALF'),
 ('ALGOL_58', 'ALGOL_58'),
 ('ALGOL_60', 'ALGOL_60'),
 ('ALGOL_68', 'ALGOL_68'),
 ('ALGOL_W', 'ALGOL_W'),
 ('Alice', 'Alice'),
 ('Alma-0', 'Alma-0'),
 ('AmbientTalk', 'AmbientTalk'),
 ('Amiga_E', 'Amiga_E'),
 ('AMOS', 'AMOS'),
 ('AMPL', 'AMPL'),
 ('APL', 'APL'),
 ("App_Inventor_for_Android's_visual_block_language",
  "App_Inventor_for_Android's_visual_block_language"),
 ('AppleScript', 'AppleScript'),
 ('Arc', 'Arc'),
 ('ARexx', 'ARexx'),
 ('Argus', 'Argus'),
 ('AspectJ', 'AspectJ'),
 ('Assembly_language', 'Assembly_language'),
 ('ATS', 'ATS'),
 ('Ateji_PX', 'Ateji_PX'),
 ('AutoHotkey', 'AutoHotkey'),
 ('Autocoder', 'Autocoder'),
 ('AutoIt', 'AutoIt'),
 ('AutoLISP_/_Visual_LISP', 'AutoLISP_/_Visual_LISP'),
 ('Averest', 'Averest'),
 ('AWK', 'AWK'),
 ('Axum', 'Axum'),
 ('B', 'B'),
 ('Babbage', 'Babbage'),
 ('Bash', 'Bash'),
 ('BASIC', 'BASIC'),
 ('bc', 'bc'),
 ('BCPL', 'BCPL'),
 ('BeanShell', 'BeanShell'),
 ('Batch_(Windows/Dos)', 'Batch_(Windows/Dos)'),
 ('Bertrand', 'Bertrand'),
 ('BETA', 'BETA'),
 ('Bigwig', 'Bigwig'),
 ('Bistro', 'Bistro'),
 ('BitC', 'BitC'),
 ('BLISS', 'BLISS'),
 ('Blue', 'Blue'),
 ('Bon', 'Bon'),
 ('Boo', 'Boo'),
 ('Boomerang', 'Boomerang'),
 ('Bourne_shell', 'Bourne_shell'),
 ('bash', 'bash'),
 ('ksh', 'ksh'),
 ('BREW', 'BREW'),
 ('BPEL', 'BPEL'),
 ('C', 'C'),
 ('C--', 'C--'),
 ('C++', 'C++'),
 ('C#', 'C#'),
 ('C/AL', 'C/AL'),
 ('C_Shell', 'C_Shell'),
 ('Caml', 'Caml'),
 ('Candle', 'Candle'),
 ('Cayenne', 'Cayenne'),
 ('CDuce', 'CDuce'),
 ('Cecil', 'Cecil'),
 ('Cel', 'Cel'),
 ('Cesil', 'Cesil'),
 ('Ceylon', 'Ceylon'),
 ('CFEngine', 'CFEngine'),
 ('CFML', 'CFML'),
 ('Cg', 'Cg'),
 ('Ch', 'Ch'),
 ('Chapel', 'Chapel'),
 ('CHAIN', 'CHAIN'),
 ('Charity', 'Charity'),
 ('Charm', 'Charm'),
 ('Chef', 'Chef'),
 ('CHILL', 'CHILL'),
 ('CHIP-8', 'CHIP-8'),
 ('chomski', 'chomski'),
 ('ChucK', 'ChucK'),
 ('CICS', 'CICS'),
 ('Cilk', 'Cilk'),
 ('CL', 'CL'),
 ('Claire', 'Claire'),
 ('Clarion', 'Clarion'),
 ('Clean', 'Clean'),
 ('Clipper', 'Clipper'),
 ('CLIST', 'CLIST'),
 ('Clojure', 'Clojure'),
 ('CLU', 'CLU'),
 ('CMS-2', 'CMS-2'),
 ('COBOL', 'COBOL'),
 ('Cobra', 'Cobra'),
 ('CODE', 'CODE'),
 ('CoffeeScript', 'CoffeeScript'),
 ('Cola', 'Cola'),
 ('ColdC', 'ColdC'),
 ('ColdFusion', 'ColdFusion'),
 ('COMAL', 'COMAL'),
 ('Combined_Programming_Language', 'Combined_Programming_Language'),
 ('COMIT', 'COMIT'),
 ('Common_Intermediate_Language', 'Common_Intermediate_Language'),
 ('Common_Lisp', 'Common_Lisp'),
 ('COMPASS', 'COMPASS'),
 ('Component_Pascal', 'Component_Pascal'),
 ('Constraint_Handling_Rules', 'Constraint_Handling_Rules'),
 ('Converge', 'Converge'),
 ('Cool', 'Cool'),
 ('Coq', 'Coq'),
 ('Coral_66', 'Coral_66'),
 ('Corn', 'Corn'),
 ('CorVision', 'CorVision'),
 ('COWSEL', 'COWSEL'),
 ('CPL', 'CPL'),
 ('csh', 'csh'),
 ('CSP', 'CSP'),
 ('Csound', 'Csound'),
 ('CUDA', 'CUDA'),
 ('Curl', 'Curl'),
 ('Curry', 'Curry'),
 ('Cyclone', 'Cyclone'),
 ('Cython', 'Cython'),
 ('D', 'D'),
 ('DASL', 'DASL'),
 ('DASL', 'DASL'),
 ('Dart', 'Dart'),
 ('DataFlex', 'DataFlex'),
 ('Datalog', 'Datalog'),
 ('DATATRIEVE', 'DATATRIEVE'),
 ('dBase', 'dBase'),
 ('dc', 'dc'),
 ('DCL', 'DCL'),
 ('Deesel', 'Deesel'),
 ('Delphi', 'Delphi'),
 ('DCL', 'DCL'),
 ('DinkC', 'DinkC'),
 ('DIBOL', 'DIBOL'),
 ('Dog', 'Dog'),
 ('Draco', 'Draco'),
 ('DRAKON', 'DRAKON'),
 ('Dylan', 'Dylan'),
 ('DYNAMO', 'DYNAMO'),
 ('E', 'E'),
 ('E#', 'E#'),
 ('Ease', 'Ease'),
 ('Easy_PL/I', 'Easy_PL/I'),
 ('Easy_Programming_Language', 'Easy_Programming_Language'),
 ('EASYTRIEVE_PLUS', 'EASYTRIEVE_PLUS'),
 ('ECMAScript', 'ECMAScript'),
 ('Edinburgh_IMP', 'Edinburgh_IMP'),
 ('EGL', 'EGL'),
 ('Eiffel', 'Eiffel'),
 ('ELAN', 'ELAN'),
 ('Elixir', 'Elixir'),
 ('Elm', 'Elm'),
 ('Emacs_Lisp', 'Emacs_Lisp'),
 ('Emerald', 'Emerald'),
 ('Epigram', 'Epigram'),
 ('EPL', 'EPL'),
 ('Erlang', 'Erlang'),
 ('es', 'es'),
 ('Escapade', 'Escapade'),
 ('Escher', 'Escher'),
 ('ESPOL', 'ESPOL'),
 ('Esterel', 'Esterel'),
 ('Etoys', 'Etoys'),
 ('Euclid', 'Euclid'),
 ('Euler', 'Euler'),
 ('Euphoria', 'Euphoria'),
 ('EusLisp_Robot_Programming_Language', 'EusLisp_Robot_Programming_Language'),
 ('CMS_EXEC', 'CMS_EXEC'),
 ('EXEC_2', 'EXEC_2'),
 ('Executable_UML', 'Executable_UML'),
 ('F', 'F'),
 ('F#', 'F#'),
 ('Factor', 'Factor'),
 ('Falcon', 'Falcon'),
 ('Fancy', 'Fancy'),
 ('Fantom', 'Fantom'),
 ('FAUST', 'FAUST'),
 ('Felix', 'Felix'),
 ('Ferite', 'Ferite'),
 ('FFP', 'FFP'),
 ('FL', 'FL'),
 ('Flavors', 'Flavors'),
 ('Flex', 'Flex'),
 ('FLOW-MATIC', 'FLOW-MATIC'),
 ('FOCAL', 'FOCAL'),
 ('FOCUS', 'FOCUS'),
 ('FOIL', 'FOIL'),
 ('FORMAC', 'FORMAC'),
 ('@Formula', '@Formula'),
 ('Forth', 'Forth'),
 ('Fortran', 'Fortran'),
 ('Fortress', 'Fortress'),
 ('FoxBase', 'FoxBase'),
 ('FoxPro', 'FoxPro'),
 ('FP', 'FP'),
 ('FPr', 'FPr'),
 ('Franz_Lisp', 'Franz_Lisp'),
 ('F-Script', 'F-Script'),
 ('FSProg', 'FSProg'),
 ('G', 'G'),
 ('Google_Apps_Script', 'Google_Apps_Script'),
 ('Game_Maker_Language', 'Game_Maker_Language'),
 ('GameMonkey_Script', 'GameMonkey_Script'),
 ('GAMS', 'GAMS'),
 ('GAP', 'GAP'),
 ('G-code', 'G-code'),
 ('Genie', 'Genie'),
 ('GDL', 'GDL'),
 ('Gibiane', 'Gibiane'),
 ('GJ', 'GJ'),
 ('GEORGE', 'GEORGE'),
 ('GLSL', 'GLSL'),
 ('GNU_E', 'GNU_E'),
 ('GM', 'GM'),
 ('Go', 'Go'),
 ('Go!', 'Go!'),
 ('GOAL', 'GOAL'),
 ('Godiva', 'Godiva'),
 ('GOM_(Good_Old_Mad)', 'GOM_(Good_Old_Mad)'),
 ('Goo', 'Goo'),
 ('Gosu', 'Gosu'),
 ('GOTRAN', 'GOTRAN'),
 ('GPSS', 'GPSS'),
 ('GraphTalk', 'GraphTalk'),
 ('GRASS', 'GRASS'),
 ('Groovy', 'Groovy'),
 ('Hack_(programming_language)', 'Hack_(programming_language)'),
 ('HAL/S', 'HAL/S'),
 ('Hamilton_C_shell', 'Hamilton_C_shell'),
 ('Harbour', 'Harbour'),
 ('Hartmann_pipelines', 'Hartmann_pipelines'),
 ('Haskell', 'Haskell'),
 ('Haxe', 'Haxe'),
 ('High_Level_Assembly', 'High_Level_Assembly'),
 ('HLSL', 'HLSL'),
 ('Hop', 'Hop'),
 ('Hope', 'Hope'),
 ('Hugo', 'Hugo'),
 ('Hume', 'Hume'),
 ('HyperTalk', 'HyperTalk'),
 ('IBM_Basic_assembly_language', 'IBM_Basic_assembly_language'),
 ('IBM_HAScript', 'IBM_HAScript'),
 ('IBM_Informix-4GL', 'IBM_Informix-4GL'),
 ('IBM_RPG', 'IBM_RPG'),
 ('ICI', 'ICI'),
 ('Icon', 'Icon'),
 ('Id', 'Id'),
 ('IDL', 'IDL'),
 ('Idris', 'Idris'),
 ('IMP', 'IMP'),
 ('Inform', 'Inform'),
 ('Io', 'Io'),
 ('Ioke', 'Ioke'),
 ('IPL', 'IPL'),
 ('IPTSCRAE', 'IPTSCRAE'),
 ('ISLISP', 'ISLISP'),
 ('ISPF', 'ISPF'),
 ('ISWIM', 'ISWIM'),
 ('J', 'J'),
 ('J#', 'J#'),
 ('J++', 'J++'),
 ('JADE', 'JADE'),
 ('Jako', 'Jako'),
 ('JAL', 'JAL'),
 ('Janus', 'Janus'),
 ('JASS', 'JASS'),
 ('Java', 'Java'),
 ('JavaScript', 'JavaScript'),
 ('JCL', 'JCL'),
 ('JEAN', 'JEAN'),
 ('Join_Java', 'Join_Java'),
 ('JOSS', 'JOSS'),
 ('Joule', 'Joule'),
 ('JOVIAL', 'JOVIAL'),
 ('Joy', 'Joy'),
 ('JScript', 'JScript'),
 ('JScript_.NET', 'JScript_.NET'),
 ('JavaFX_Script', 'JavaFX_Script'),
 ('Julia', 'Julia'),
 ('Jython', 'Jython'),
 ('K', 'K'),
 ('Kaleidoscope', 'Kaleidoscope'),
 ('Karel', 'Karel'),
 ('Karel++', 'Karel++'),
 ('KEE', 'KEE'),
 ('Kixtart', 'Kixtart'),
 ('KIF', 'KIF'),
 ('Kojo', 'Kojo'),
 ('Kotlin', 'Kotlin'),
 ('KRC', 'KRC'),
 ('KRL', 'KRL'),
 ('KUKA', 'KUKA'),
 ('KRYPTON', 'KRYPTON'),
 ('ksh', 'ksh'),
 ('L', 'L'),
 ('L#_.NET', 'L#_.NET'),
 ('LabVIEW', 'LabVIEW'),
 ('Ladder', 'Ladder'),
 ('Lagoona', 'Lagoona'),
 ('LANSA', 'LANSA'),
 ('Lasso', 'Lasso'),
 ('LaTeX', 'LaTeX'),
 ('Lava', 'Lava'),
 ('LC-3', 'LC-3'),
 ('Leda', 'Leda'),
 ('Legoscript', 'Legoscript'),
 ('LIL', 'LIL'),
 ('LilyPond', 'LilyPond'),
 ('Limbo', 'Limbo'),
 ('Limnor', 'Limnor'),
 ('LINC', 'LINC'),
 ('Lingo', 'Lingo'),
 ('Linoleum', 'Linoleum'),
 ('LIS', 'LIS'),
 ('LISA', 'LISA'),
 ('Lisaac', 'Lisaac'),
 ('Lisp', 'Lisp'),
 ('Lite-C', 'Lite-C'),
 ('Lithe', 'Lithe'),
 ('Little_b', 'Little_b'),
 ('Logo', 'Logo'),
 ('Logtalk', 'Logtalk'),
 ('LPC', 'LPC'),
 ('LSE', 'LSE'),
 ('LSL', 'LSL'),
 ('LiveCode', 'LiveCode'),
 ('LiveScript', 'LiveScript'),
 ('Lua', 'Lua'),
 ('Lucid', 'Lucid'),
 ('Lustre', 'Lustre'),
 ('LYaPAS', 'LYaPAS'),
 ('Lynx', 'Lynx'),
 ('M2001', 'M2001'),
 ('M4', 'M4'),
 ('Machine_code', 'Machine_code'),
 ('MAD', 'MAD'),
 ('MAD/I', 'MAD/I'),
 ('Magik', 'Magik'),
 ('Magma', 'Magma'),
 ('make', 'make'),
 ('Maple', 'Maple'),
 ('MAPPER', 'MAPPER'),
 ('MARK-IV', 'MARK-IV'),
 ('Mary', 'Mary'),
 ('MASM_Microsoft_Assembly_x86', 'MASM_Microsoft_Assembly_x86'),
 ('Mathematica', 'Mathematica'),
 ('MATLAB', 'MATLAB'),
 ('Maxima', 'Maxima'),
 ('Macsyma', 'Macsyma'),
 ('Max', 'Max'),
 ('MaxScript', 'MaxScript'),
 ('Maya_(MEL)', 'Maya_(MEL)'),
 ('MDL', 'MDL'),
 ('Mercury', 'Mercury'),
 ('Mesa', 'Mesa'),
 ('Metacard', 'Metacard'),
 ('Metafont', 'Metafont'),
 ('MetaL', 'MetaL'),
 ('Microcode', 'Microcode'),
 ('MicroScript', 'MicroScript'),
 ('MIIS', 'MIIS'),
 ('MillScript', 'MillScript'),
 ('MIMIC', 'MIMIC'),
 ('Mirah', 'Mirah'),
 ('Miranda', 'Miranda'),
 ('MIVA_Script', 'MIVA_Script'),
 ('ML', 'ML'),
 ('Moby', 'Moby'),
 ('Model_204', 'Model_204'),
 ('Modelica', 'Modelica'),
 ('Modula', 'Modula'),
 ('Modula-2', 'Modula-2'),
 ('Modula-3', 'Modula-3'),
 ('Mohol', 'Mohol'),
 ('MOO', 'MOO'),
 ('Mortran', 'Mortran'),
 ('Mouse', 'Mouse'),
 ('MPD', 'MPD'),
 ('CIL', 'CIL'),
 ('MSL', 'MSL'),
 ('MUMPS', 'MUMPS'),
 ('NASM', 'NASM'),
 ('NATURAL', 'NATURAL'),
 ('Napier88', 'Napier88'),
 ('Neko', 'Neko'),
 ('Nemerle', 'Nemerle'),
 ('nesC', 'nesC'),
 ('NESL', 'NESL'),
 ('Net.Data', 'Net.Data'),
 ('NetLogo', 'NetLogo'),
 ('NetRexx', 'NetRexx'),
 ('NewLISP', 'NewLISP'),
 ('NEWP', 'NEWP'),
 ('Newspeak', 'Newspeak'),
 ('NewtonScript', 'NewtonScript'),
 ('NGL', 'NGL'),
 ('Nial', 'Nial'),
 ('Nice', 'Nice'),
 ('Nickle', 'Nickle'),
 ('NPL', 'NPL'),
 ('Not_eXactly_C', 'Not_eXactly_C'),
 ('Not_Quite_C', 'Not_Quite_C'),
 ('NSIS', 'NSIS'),
 ('Nu', 'Nu'),
 ('NWScript', 'NWScript'),
 ('NXT-G', 'NXT-G'),
 ('o:XML', 'o:XML'),
 ('Oak', 'Oak'),
 ('Oberon', 'Oberon'),
 ('Obix', 'Obix'),
 ('OBJ2', 'OBJ2'),
 ('Object_Lisp', 'Object_Lisp'),
 ('ObjectLOGO', 'ObjectLOGO'),
 ('Object_REXX', 'Object_REXX'),
 ('Object_Pascal', 'Object_Pascal'),
 ('Objective-C', 'Objective-C'),
 ('Objective-J', 'Objective-J'),
 ('Obliq', 'Obliq'),
 ('Obol', 'Obol'),
 ('OCaml', 'OCaml'),
 ('occam', 'occam'),
 ('Octave', 'Octave'),
 ('OmniMark', 'OmniMark'),
 ('Onyx', 'Onyx'),
 ('Opa', 'Opa'),
 ('Opal', 'Opal'),
 ('OpenCL', 'OpenCL'),
 ('OpenEdge_ABL', 'OpenEdge_ABL'),
 ('OPL', 'OPL'),
 ('OPS5', 'OPS5'),
 ('OptimJ', 'OptimJ'),
 ('Orc', 'Orc'),
 ('ORCA/Modula-2', 'ORCA/Modula-2'),
 ('Oriel', 'Oriel'),
 ('Orwell', 'Orwell'),
 ('Oxygene', 'Oxygene'),
 ('Oz', 'Oz'),
 ('P#', 'P#'),
 ('ParaSail_(programming_language)', 'ParaSail_(programming_language)'),
 ('PARI/GP', 'PARI/GP'),
 ('Pascal', 'Pascal'),
 ('Pawn', 'Pawn'),
 ('PCASTL', 'PCASTL'),
 ('PCF', 'PCF'),
 ('PEARL', 'PEARL'),
 ('PeopleCode', 'PeopleCode'),
 ('Perl', 'Perl'),
 ('PDL', 'PDL'),
 ('PHP', 'PHP'),
 ('Phrogram', 'Phrogram'),
 ('Pico', 'Pico'),
 ('Picolisp', 'Picolisp'),
 ('Pict', 'Pict'),
 ('Pike', 'Pike'),
 ('PIKT', 'PIKT'),
 ('PILOT', 'PILOT'),
 ('Pipelines', 'Pipelines'),
 ('Pizza', 'Pizza'),
 ('PL-11', 'PL-11'),
 ('PL/0', 'PL/0'),
 ('PL/B', 'PL/B'),
 ('PL/C', 'PL/C'),
 ('PL/I', 'PL/I'),
 ('PL/M', 'PL/M'),
 ('PL/P', 'PL/P'),
 ('PL/SQL', 'PL/SQL'),
 ('PL360', 'PL360'),
 ('PLANC', 'PLANC'),
 ('Planner', 'Planner'),
 ('PLEX', 'PLEX'),
 ('PLEXIL', 'PLEXIL'),
 ('Plus', 'Plus'),
 ('POP-11', 'POP-11'),
 ('PostScript', 'PostScript'),
 ('PortablE', 'PortablE'),
 ('Powerhouse', 'Powerhouse'),
 ('PowerBuilder', 'PowerBuilder'),
 ('PowerShell', 'PowerShell'),
 ('PPL', 'PPL'),
 ('Processing', 'Processing'),
 ('Processing.js', 'Processing.js'),
 ('Prograph', 'Prograph'),
 ('PROIV', 'PROIV'),
 ('Prolog', 'Prolog'),
 ('PROMAL', 'PROMAL'),
 ('Promela', 'Promela'),
 ('PROSE_modeling_language', 'PROSE_modeling_language'),
 ('PROTEL', 'PROTEL'),
 ('ProvideX', 'ProvideX'),
 ('Pro*C', 'Pro*C'),
 ('Pure', 'Pure'),
 ('Python', 'Python'),
 ('Q_(equational_programming_language)',
  'Q_(equational_programming_language)'),
 ('Q_(programming_language_from_Kx_Systems)',
  'Q_(programming_language_from_Kx_Systems)'),
 ('Qalb', 'Qalb'),
 ('Qi', 'Qi'),
 ('QtScript', 'QtScript'),
 ('QuakeC', 'QuakeC'),
 ('QPL', 'QPL'),
 ('R', 'R'),
 ('R++', 'R++'),
 ('Racket', 'Racket'),
 ('RAPID', 'RAPID'),
 ('Rapira', 'Rapira'),
 ('Ratfiv', 'Ratfiv'),
 ('Ratfor', 'Ratfor'),
 ('rc', 'rc'),
 ('REBOL', 'REBOL'),
 ('Red', 'Red'),
 ('Redcode', 'Redcode'),
 ('REFAL', 'REFAL'),
 ('Reia', 'Reia'),
 ('Revolution', 'Revolution'),
 ('rex', 'rex'),
 ('REXX', 'REXX'),
 ('Rlab', 'Rlab'),
 ('RobotC', 'RobotC'),
 ('ROOP', 'ROOP'),
 ('RPG', 'RPG'),
 ('RPL', 'RPL'),
 ('RSL', 'RSL'),
 ('RTL/2', 'RTL/2'),
 ('Ruby', 'Ruby'),
 ('RuneScript', 'RuneScript'),
 ('Rust', 'Rust'),
 ('S', 'S'),
 ('S2', 'S2'),
 ('S3', 'S3'),
 ('S-Lang', 'S-Lang'),
 ('S-PLUS', 'S-PLUS'),
 ('SA-C', 'SA-C'),
 ('SabreTalk', 'SabreTalk'),
 ('SAIL', 'SAIL'),
 ('SALSA', 'SALSA'),
 ('SAM76', 'SAM76'),
 ('SAS', 'SAS'),
 ('SASL', 'SASL'),
 ('Sather', 'Sather'),
 ('Sawzall', 'Sawzall'),
 ('SBL', 'SBL'),
 ('Scala', 'Scala'),
 ('Scheme', 'Scheme'),
 ('Scilab', 'Scilab'),
 ('Scratch', 'Scratch'),
 ('Script.NET', 'Script.NET'),
 ('Sed', 'Sed'),
 ('Seed7', 'Seed7'),
 ('Self', 'Self'),
 ('SenseTalk', 'SenseTalk'),
 ('SequenceL', 'SequenceL'),
 ('SETL', 'SETL'),
 ('Shift_Script', 'Shift_Script'),
 ('SIMPOL', 'SIMPOL'),
 ('Shakespeare', 'Shakespeare'),
 ('SIGNAL', 'SIGNAL'),
 ('SiMPLE', 'SiMPLE'),
 ('SIMSCRIPT', 'SIMSCRIPT'),
 ('Simula', 'Simula'),
 ('Simulink', 'Simulink'),
 ('SISAL', 'SISAL'),
 ('SLIP', 'SLIP'),
 ('SMALL', 'SMALL'),
 ('Smalltalk', 'Smalltalk'),
 ('Small_Basic', 'Small_Basic'),
 ('SML', 'SML'),
 ('Snap!', 'Snap!'),
 ('SNOBOL', 'SNOBOL'),
 ('SPITBOL', 'SPITBOL'),
 ('Snowball', 'Snowball'),
 ('SOL', 'SOL'),
 ('Span', 'Span'),
 ('SPARK', 'SPARK'),
 ('SPIN', 'SPIN'),
 ('SP/k', 'SP/k'),
 ('SPS', 'SPS'),
 ('Squeak', 'Squeak'),
 ('Squirrel', 'Squirrel'),
 ('SR', 'SR'),
 ('S/SL', 'S/SL'),
 ('Stackless_Python', 'Stackless_Python'),
 ('Starlogo', 'Starlogo'),
 ('Strand', 'Strand'),
 ('Stata', 'Stata'),
 ('Stateflow', 'Stateflow'),
 ('Subtext', 'Subtext'),
 ('SuperCollider', 'SuperCollider'),
 ('SuperTalk', 'SuperTalk'),
 ('Swift_(Apple_programming_language)', 'Swift_(Apple_programming_language)'),
 ('Swift_(parallel_scripting_language)',
  'Swift_(parallel_scripting_language)'),
 ('SYMPL', 'SYMPL'),
 ('SyncCharts', 'SyncCharts'),
 ('SystemVerilog', 'SystemVerilog'),
 ('T', 'T'),
 ('TACL', 'TACL'),
 ('TACPOL', 'TACPOL'),
 ('TADS', 'TADS'),
 ('TAL', 'TAL'),
 ('Tcl', 'Tcl'),
 ('Tea', 'Tea'),
 ('TECO', 'TECO'),
 ('TELCOMP', 'TELCOMP'),
 ('TeX', 'TeX'),
 ('TEX', 'TEX'),
 ('TIE', 'TIE'),
 ('Timber', 'Timber'),
 ('TMG', 'TMG'),
 ('Tom', 'Tom'),
 ('TOM', 'TOM'),
 ('Topspeed', 'Topspeed'),
 ('TPU', 'TPU'),
 ('Trac', 'Trac'),
 ('TTM', 'TTM'),
 ('T-SQL', 'T-SQL'),
 ('TTCN', 'TTCN'),
 ('Turing', 'Turing'),
 ('TUTOR', 'TUTOR'),
 ('TXL', 'TXL'),
 ('TypeScript', 'TypeScript'),
 ('Turbo_C++', 'Turbo_C++'),
 ('Ubercode', 'Ubercode'),
 ('UCSD_Pascal', 'UCSD_Pascal'),
 ('Umple', 'Umple'),
 ('Unicon', 'Unicon'),
 ('Uniface', 'Uniface'),
 ('UNITY', 'UNITY'),
 ('Unix_shell', 'Unix_shell'),
 ('UnrealScript', 'UnrealScript'),
 ('Vala', 'Vala'),
 ('VBA', 'VBA'),
 ('VBScript', 'VBScript'),
 ('Verilog', 'Verilog'),
 ('VHDL', 'VHDL'),
 ('Visual_Basic', 'Visual_Basic'),
 ('Visual_Basic_.NET', 'Visual_Basic_.NET'),
 ('Visual_DataFlex', 'Visual_DataFlex'),
 ('Visual_DialogScript', 'Visual_DialogScript'),
 ('Visual_Fortran', 'Visual_Fortran'),
 ('Visual_FoxPro', 'Visual_FoxPro'),
 ('Visual_J++', 'Visual_J++'),
 ('Visual_J#', 'Visual_J#'),
 ('Visual_Objects', 'Visual_Objects'),
 ('Visual_Prolog', 'Visual_Prolog'),
 ('VSXu', 'VSXu'),
 ('Vvvv', 'Vvvv'),
 ('WATFIV,_WATFOR', 'WATFIV,_WATFOR'),
 ('WebDNA', 'WebDNA'),
 ('WebQL', 'WebQL'),
 ('Windows_PowerShell', 'Windows_PowerShell'),
 ('Winbatch', 'Winbatch'),
 ('Wolfram', 'Wolfram'),
 ('Wyvern', 'Wyvern'),
 ('X++', 'X++'),
 ('X#', 'X#'),
 ('X10', 'X10'),
 ('XBL', 'XBL'),
 ('XC', 'XC'),
 ('XMOS_architecture', 'XMOS_architecture'),
 ('xHarbour', 'xHarbour'),
 ('XL', 'XL'),
 ('Xojo', 'Xojo'),
 ('XOTcl', 'XOTcl'),
 ('XPL', 'XPL'),
 ('XPL0', 'XPL0'),
 ('XQuery', 'XQuery'),
 ('XSB', 'XSB'),
 ('XSLT', 'XSLT'),
 ('XPath', 'XPath'),
 ('Xtend', 'Xtend'),
 ('Yorick', 'Yorick'),
 ('YQL', 'YQL'),
 ('Z_notation', 'Z_notation'),
 ('Zeno', 'Zeno'),
 ('ZOPL', 'ZOPL'),
 ('ZPL', 'ZPL'))


class Snippet(Basemodel):
    name = models.CharField(max_length=200, blank=True, null=True)
    source_url = models.CharField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=200, blank=True, null=True, choices=LANGUAGES)
    type = models.CharField(max_length=200, blank=True, null=True, choices=TYPE)
    desc = models.TextField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)