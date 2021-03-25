# Generic file to learn Python's syntax.

from random import randint, seed
from re import findall, search, split, sub
import unicodedata
from binascii import unhexlify
from datetime import date
from time import time, ctime, sleep, struct_time, mktime
from os.path import exists
from shutil import copy
from os import rename, remove, listdir
from csv import list_dialects, reader
from pandas import read_csv, DataFrame
from requests import get
import urllib.request as ur
import logging


prince = 99
print ( "Variable 'prince' has the type " + str ( type ( prince ) ) )
print ( "The type of the expression '5' is " + str ( type ( 5 ) ) )
print ( "The type of the expression '2.0' is " + str ( type ( 2.0 ) ) )
secondsPerHour = 60 * 60
secondsPerDay = secondsPerHour * 24
print ( "In an hour there are", secondsPerHour, "seconds." )
print ( "In a day there are", secondsPerDay, "seconds." )
print ( secondsPerDay / secondsPerHour )
print ( secondsPerDay // secondsPerHour )
print ( 3 ** 2 )
print ( int ( 3.1416 ) )
print ( float ( 2 ) )
myNumbers = '012345'
theNumber = '7'
secret = 5
guess = 5
if guess < secret :
    print ( "Too low." )
elif guess > secret :
    print ( "Too high." )
else :
    print ( "Just right." )
###########################################################################################################
small = True
green = True
if small == True and green == True :
    print ( "It's a pea." )
elif small == True and green == False :
    print ( "It's a cherry." )
elif small == False and green == False :
    print ( "It's a pumpkin." )
else :
    print ( "It's a watermelon." )
string1 = 'First string.'
string2 = "Second string."
string3 = "A three times string.\n" * 3
print ( string1 )
print ( string1, string2 )
print ( string1 [ 2 ] )
print ( string3 )
if string1 == "First string." :
    print ( "string1 indeed is the first string." )
else :
    print ( "string2 is not the first string." )
###########################################################################################################
print ( 'string1 length is', len ( string1 ) )
replacedString = string1.replace ( 'First', 'First replaced' )
newString = 'A new string indeed, to test some basic string functions.'
print ( 'Number of appearances of to in newString', newString.count ( 'to' ) )
print ( 'Index of basic in newString', newString.index ( 'basic' ) )
###########################################################################################################
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
print ( song.replace ( ' m', ' M' ) )
questions = [ "We don't serve strings aroud here. Are you a string?\n", "What is said on Father's Day in the forest?\n",
"Whats makes the sound 'Sis! Boom! Bah!'?\n" ]
answers = [ "An exploding sheep.", "No, I'm a frayed knot.", "'Pop!' goes the weasel." ]
print ( 'Q:', questions [ 0 ] + 'A:', answers [ 1 ] )
print ( 'Q:', questions [ 1 ] + 'A:', answers [ 2 ] )
print ( 'Q:', questions [ 2 ] + 'A:', answers [ 0 ] )
roastBeef = 'roast beef'
ham = 'ham'
head = 'head'
clam = 'clam'
print ( "My kitty cat likes %s\nMy kitty cat likes %s\nMy kitty cat fell on his %s\nAnd now he thinks he's a %s\n" % ( roastBeef, ham, head, clam ) )
salutation = "Prof. Dr."
name = "Thomas Knabner"
product = "battery"
verbed = "exploded"
room = "bathroom"
animals = "cats"
amount = "USD 49.99"
percent = "95"
spokesman = "George Z."
job_title = "Junior engineer."
letter = F"""Dear { salutation } { name },

Thank you for your letter. We are sorry that our { product }
{ verbed } in your { room }. Please note that it should never
be used in a { room }, especially near any { animals }.

Send us your receipt and { amount } for shipping and handling.
We will send you another { product } that, in our tests,
is { percent }% less likely to have { verbed }.

Thank you for your support.

Sincerely,
{ spokesman }
{ job_title }"""
print ( letter.format() )
###########################################################################################################
y = 'y'
face = 'Face'
print ( "---The winners are, with the old style---" )
print ( "Duck%s " % y + "McDuck%s" % face )
print ( "Gourd%s " % y + "McGourd%s" % face )
print ( "Spitz%s " % y + "McSpitz%s" % face )
print ( "---The winners are, now with format()---" )
print ( "Duck{} McDuck{}".format ( y, face ) )
print ( "Gourd{} McGourd{}".format ( y, face ) )
print ( "Spitz{} McSpitz{}".format ( y, face ) )
print ( "---The winners are, now with F-strings---" )
print ( F"Duck{ y } McDuck{ face }" )
print ( F"Gourd{ y } McGourd{ face }" )
print ( F"Spitz{ y } McSpitz{ face }" )
###########################################################################################################
myList = [ 3, 2, 1, 0 ]
for data in myList :
    print ( data )
guess_me = 7
number = 1
while number <= guess_me :
    if number < guess_me :
        print ( "too low" )
    elif number == guess_me :
        print ( "found it!" )
        break
    else :
        print ( "oops" )
        break
    number += 1
guess_me5 = 5
print ( "\n\n" )
for number in range ( 10 ) :
    if number < guess_me5 :
        print ( "too low" )
    elif number == guess_me5 :
        print ( "found it!" )
        break
    else :
        print ( "oops" )
        break
###########################################################################################################
firstTuple = ( '5', '8', '9', '9', '0', '3' )
firstList = [ 5, 2, 9, 3, 11, 7 ]
secondList = []
thirdList = []
fourthList = thirdList
n = 50
for data in range ( n ) :
    seed ( data )
    secondList.append ( randint ( 0, 100 ) )
print ( "fourthList before for loop:\n", fourthList )
for data in range ( n ) :
    seed ( data )
    thirdList.append ( randint ( 0, 1000 ) )
print ( "\n" )
print ( "fourthList after for loop:\n", fourthList )
compList = [ data for data in range ( 1, 10 ) ]
compListOdds = [ data for data in range ( 1, 10 ) if data % 2 == 1 ]
print ( "Comprehension list:", compList )
print ( "Comprehension list of odds:", compListOdds )
###########################################################################################################
years_list = [ 1999, 2000, 2001, 2002, 2003 ]
print ( "My third birthday was at the year", years_list [ 3 ] )
print ( "I was oldest at the year", years_list [ 4 ] )
things = [ 'mozzarella', 'cinderella', 'salmonella' ]
things [ 1 ] = things [ 1 ].capitalize()
print ( things )
things [ 0 ] = things [ 0 ].upper()
print ( things )
del things [ 2 ]
print ( things )
surprise = [ 'Groucho', 'Chico', 'Harpo' ]
surprise [ 2 ] = surprise [ 2 ].lower()
surprise [ 2 ] = surprise [ 2 ].upper()
surprise [ 2 ] = surprise [ 2 ].capitalize()
print ( surprise )
even = [ data for data in range ( 1, 10 ) if data % 2 == 0 ]
print ( even )
start1 = [ "fee", "fie", "foe" ]
rhymes = [
    ( "flop", "get a mop" ),
    ( "fope", "turn the rope" ),
    ( "fa", "get your ma" ),
    ( "fudge", "call the judge" ),
    ( "fat", "pet the cat" ),
    ( "fog", "walk the dog" ),
    ( "fun", "say we're done" ),
    ]
start2 = "Someone better"
for data in rhymes :
    print ( ( start1 [ 0 ] + "! " + start1 [ 1 ] + "! " + start1 [ 2 ] + "!" ).title(), data [ 0 ].capitalize() + "!" )
    print ( start2, data [ 1 ] + "." )
firstDict = { '0' : 'zero', '1' : 'one', '2': 'two', '3' : 'three', '4' : 'four' }
print ( firstDict [ '2' ] )
print ( len ( firstDict ) )
print ( firstDict.keys() )
print ( firstDict.values() )
print ( '3' in firstDict )
firstSet = { 1, 2, 3, 4, 5 }
print ( "firstSet length", len ( firstSet ) )
print ( "10 is in firstSet:", 10 in firstSet )
for data in firstSet :
    print ( data )
firstSet.add ( 10 )
print ( "10 is in firstSet:", 10 in firstSet )
print ( type ( firstSet ) )
newSet = set ()
newSet.add ( 4 )
newSet.add ( 'n' )
newSet.add ( ( 3, 1 ) )
print ( newSet )
print ( len ( newSet ) )
for data in newSet :
    print ( data )
###########################################################################################################
e2f = { 'dog' : 'chien', 'cat': 'chat', 'walrus' : 'morse' }
print ( e2f [ 'walrus' ] )
f2e = {}
for english, french in e2f.items() :
    f2e [ french ] = english
print ( f2e [ 'chien' ] )
print ( e2f.keys() )
cats = [ 'Henry', 'Grumpy', 'Lucy' ]
animals = { 'cats': cats, 'octopi': {}, 'emu': {} }
life = { 'animals': animals, 'plants': {}, 'other': {} }
print ( life.keys() )
print ( life [ 'animals' ].keys() )
print ( life [ 'animals' ] [ 'cats'] )
squareNum = 0
squares = { key: key ** 2 for key in range ( 10 ) }
print ( squares )
odd = { element for element in range ( 10 ) if element % 2 != 0 }
print ( odd )
keysTuple = ( 'optimist', 'pessimist', 'troll' )
valuesTuple = ( 'The glass is half full', 'The glass is half empty', 'How did you get a glass?' )
dictionary = {  person : phrase for person, phrase in zip ( keysTuple, valuesTuple ) }
titles = [ 'Creature of habit', ' Crewel Fate', 'Sharks On a Plane' ]
plots = [ 'A nun turns into a monster', 'A haunted yarn shop', 'Check your exits' ]
movies = { movie : plot for  movie, plot in zip ( titles, plots ) }
print ( dictionary )
print ( movies )
print ( "firstList id:", id ( firstList ) )
print ( "secondList id:", id ( secondList ) )
def good() :
    return [ 'Harry', 'Ron', 'Hermione' ]
def get_odds () :
    odds = [ data for data in range ( 10 ) if data % 2 != 0 ]
    return odds
for i in range ( 0, len ( get_odds() ) ) :
    if i == 2 :
        print  ( get_odds() [ i ] )
def test ( fun ) :
    def new_function ( * a, ** b ) :
        print ( "start" )
        fun ( * a, ** b )
        print ( "end" )
    return new_function
@test
def add_ints ( a, b ) :
    print ( a + b )
add_ints ( 5, 9 )
class OopsException ( Exception ):
    pass
try :
    raise OopsException ( 'Caught an oops' )
except OopsException as exception :
    print ( exception )
class Thing :
    pass
example = Thing()
print ( Thing )
print ( example )
class Thing2 :
    letters = 'abc'
print ( Thing2.letters )
class Thing3 :
    def __init__ ( self, letters ) :
        self.letters = letters
newObject = Thing3 ( 'xyz' )
class Element :
    def __init__ ( self, name, symbol, number ) :
        self.__name = name
        self.__symbol = symbol
        self.__number = number
    @property
    def name ( self ) :
        print ( "Name:  ", self.__name )
    @property
    def symbol ( self ) :
        print ( "Symbol:", self.__symbol )
    @property
    def number ( self ) :
        print ( "Number:", self.__number )
    def __str__ ( self ) :
        return "Name:   " + self.__name + "\nSymbol: " + self.__symbol + "\nNumber: " + self.__number
element = Element ( 'Hydrogen', 'H', '1' )
dictHydr = { 'name' : 'Hydrogen', 'symbol' : 'H', 'number' : '1' }
hydrogen = Element ( ** dictHydr )
print ( newObject.letters )
hydrogen2 = Element ( 'Hydrogen', 'H', '1' )
print ( hydrogen2 )
hydrogen2.name
hydrogen2.symbol
hydrogen2.number
class Bear :
    def eats ( self ) :
        print ( self.food )
class Rabbit :
    def eats ( self ) :
        print ( self.food )
class Octothorpe :
    def eats ( self ) :
        print ( self.food )
bear = Bear ()
rabbit = Rabbit ()
octothorpe = Octothorpe ()
bear.food = 'berries'
rabbit.food = 'clover'
octothorpe.food = 'campers'
bear.eats()
rabbit.eats()
octothorpe.eats()
class Laser :
    def does ( self ) :
        return 'disintegrate'
class Claw :
    def does ( self ) :
        return 'crush'
class SmartPhone :
    def does ( self ) :
        return 'ring'
class Robot :
    laser = Laser()
    claw = Claw()
    smartphone = SmartPhone()
    def does ( cls ) :
        print ( "Laser object does", cls.laser.does() )
        print ( "Claw object does", cls.claw.does() )
        print ( "SmartPhone object does", cls.smartphone.does() )
robot = Robot()
robot.does()
print ( "Hallo der \u042F" )
regularExpression = "It is indeed a lovely day, isn't it?"
a = findall ( 'is', regularExpression )
b = search ( 'lov', regularExpression )
c = split ( 'lovely', regularExpression )
d = sub ( 'lovely', 'horrible', regularExpression )
print ( a )
print ( b.start() )
print ( c )
print ( d )
mystery = '\U0001f984'
print ( mystery, unicodedata.name ( mystery ) )
pop_bytes =  mystery.encode ( 'utf-8' )
print ( pop_bytes )
pop_string = pop_bytes.decode ( 'utf-8' )
print ( pop_string )
print ( "pop_bytes == pop_string?", pop_bytes == pop_string )
mammoth = '''We have seen thee, queen of cheese,
        Lying quietly at your ease,
        Gently fanned by evening breeze,
        Thy fair form no flies dare seize.

        All gaily dressed soon you'll go
        To the great Provincial show,
        To be admired by many a beau
        In the city of Toronto.

        Cows numerous as a swarm of bees,
        Or as the leaves upon the trees,
        It did require to make thee please,
        And stand unrivalled, queen of cheese.

        May you not receive a scar as
        We have heard that Mr. Harris
        Intends to send you off as far as
        The great world's show at Paris.

        Of the youth beware of these,
        For some of them might rudely squeeze
        And bite your cheek, then songs or glees
        We could not sing, oh! queen of cheese.

        We'rt thou suspended from balloon,
        You'd cast a shade even at noon,
        Folks would think it was the moon
        About to fall and crush them soon.'''
print ( findall ( 'c', mammoth ) )
print ( findall ( '\sc...\s', mammoth ) )
print ( findall ( '\b', mammoth ) )
gif = unhexlify ( '47494638396101000100800000000000ffffff21f9' +
      '0401000000002c000000000100010000020144003b' )
print ( gif )
print ( gif [ 6 ] )
print ( gif [ 8 ] )
myBirthday = date ( 1999, 9, 27 )
myBirthday2 = ( 1999, 9, 27 )
now = time()
print ( myBirthday.year, myBirthday.month, myBirthday.day )
print ( myBirthday.isoformat() )
print ( date.today() )
string = ctime ( now )
print ( type ( now ) )
sleep ( 0 )
print ( string )
print ( myBirthday.weekday() )
birth = mktime ( struct_time ( ( 1999, 9, 27, 0, 0, 0, 0, 0, 0 ) ) )
tenThousand = ctime ( birth + 10000 * 24 * 60 * 60 )
print ( "I will be ten thousand days old on", tenThousand )
#todayFile = open ( 'today.txt', 'wt' )
#print ( date.today(), file = todayFile )
#todayFile.close()
#todayFile = open ( 'today.txt', 'rt' )
#today_string = todayFile.read()
#print ( today_string )
#todayFile.close()
firstFile = open ( 'new.txt', 'at' )
print ( "First file created", file  = firstFile )
firstFile.close()
firstFile = open ( 'new.txt', 'rt' )
secondFile = firstFile.read()
print ( secondFile )
print ( "The file 'new.txt' exists:", exists ( 'new.txt' ) )
#copy ( 'new.txt', 'copied.txt' )
firstFile.close()
remove ( 'new.txt' )
print ( listdir ( '.' ) )
print ( listdir ( '..' ) )
test1 = 'This is a test of the emergency test system'
#with open ( 'test.txt', 'wt' ) as newFile :
#	print ( test1, file = newFile )
#with open ( 'test.txt', 'rt' ) as newFile2 :
#	test2 = newFile2.read()
#print ( test1 )
#print ( test2 )
COVID19 = read_csv ( "COVID19.csv" )
colList = list ( COVID19 )
colList.remove ( "poblacion" )
COVID19 [ "Casos totales" ] = COVID19 [ colList ].sum ( axis = 1 )
#print ( COVID19 )
#print ( COVID19.describe () )
print ( COVID19.info() )
print ( COVID19 [ [ "nombre", "Casos totales" ] ] )
print ( COVID19.loc [ COVID19 [ "Casos totales" ] > 30000 ] )
dataFrame = DataFrame ( { "Name": [ "Braund, Mr. Owen Harris", "Allen, Mr. William Henry", "Bonnell, Miss. Elizabeth" ],
	"Age" : [ 22, 35, 58 ] , "Sex" : [ "male", "male", "female" ] } )
print ( dataFrame )
print ( dataFrame [ "Age" ] )
url = 'https://algo.informatik.uni-freiburg.de/bibliothek/books/ad-buch/'
conn = ur.urlopen ( url )
print ( conn.status )
data = conn.read()
print ( data [ :50 ] )
str_data = data.decode ( 'utf-8', errors = "ignore" )
print ( str_data [ :50 ] )
response = get ( 'https://algo.informatik.uni-freiburg.de/bibliothek/books/ad-buch/', verify = False, auth = ( 'user', 'pass ') )
print( response.text )
logging.basicConfig ( level = 'DEBUG', filename = 'myFillename.log' )
logger = logging.getLogger ( 'myLogger' )
logger.debug ( "Sample message displayed" )
logger.warn ( "Sample warning displayed" )
wait = input ( "\nPress any key to exit..." )
