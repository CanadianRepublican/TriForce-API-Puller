#!/usr/bin/env python

from urllib.request import urlopen
import json
import MySQLdb
import datetime
import dateutil.parser
import urllib
import posixpath
import urlparse
from distutils.util import strtobool
import codecs

codecs.register_error("strict", codecs.ignore_errors)

def string_to_bool(string):
    return bool(strtobool(str(string)))

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


db = MySQLdb.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="Tr1F0rc3",     # password
                     db="triforce-lift")   # name of the database

# Create a Cursor object to execute queries.
cur = db.cursor()

#url =  ("https://lift.co/api/v2/businesses?&page=1")
url =  ("https://lift.co/api/v2/users?&page=1")

jsondata = get_jsonparsed_data(url)

print
print(jsondata['pages'])
print(jsondata['count'])
print(jsondata['page'])
print

for x in range(1, int(jsondata['pages'])+1):
  itemcount=jsondata['per_page']
  pageitem=x*jsondata['per_page']
  lastpage=jsondata['count']-pageitem
  if lastpage < 0:
    itemcount=jsondata['per_page']+lastpage

  print
  print("Page: "+str(x))
  #url =  ("https://lift.co/api/v2/businesses?&page="+str(x))
  url =  ("https://lift.co/api/v2/users?&page="+str(x))
  jsondatab = get_jsonparsed_data(url)
  for y in range(0, itemcount):
    #reset Vars
    lift_id = 0
    picture = ""
    slug = "''"
    firstName = ""
    lastName = ""
    gender = ""
    postalCode = ""
    username = ""
    lift__v = 0
    lift_id_2 = 0
    uploadedPicture = ""
    bio = '""'
    birthday = "NULL"
    facebook = ""
    twitter = ""
    gravatarPicture = ""
    achievements = '""'
    fullLocation = "''"
    address = "''"
    city = "''"
    province = "''"
    fullName = "''"
    usingCannabisSince = "NULL"
    profileCompletedOn = "NULL"
    cannabisExperience = '""'
    updatedOn = "NULL"
    createdOn = "NULL"
    verified = 0
    suspended = 0
    banned = 0
    knownConditions = '""'
    reputation = 0
    isAnonymous = 0
    helpfulReviewCount = 0
    reviewCount = 0
    role = '""'
    joindate = "NULL"
    lastOnline = "NULL"
    age = 0

    print
    print("Page: "+str(x)+" - Item: "+str(y))
    print(jsondatab['hits'][y])

    if jsondatab['hits'][y].get('role'):
      role = '"'+str(jsondatab['hits'][y]['role']).encode("utf-8", "ignore")+'"'
      print
      print str(role)
      print

    if jsondatab['hits'][y].get('knownConditions'):
      knownConditions = '"'+str(jsondatab['hits'][y]['knownConditions']).encode("utf-8", "ignore")+'"'
      print
      print str(knownConditions)
      print

    if jsondatab['hits'][y].get('cannabisExperience'):
      cannabisExperience = '"'+str(jsondatab['hits'][y]['cannabisExperience']).encode("utf-8", "ignore")+'"'
      print
      print str(cannabisExperience)
      print

    if jsondatab['hits'][y].get('city'):
      city = '"'+jsondatab['hits'][y]['city'].encode("utf-8", "ignore")+'"'
      print
      print str(city)
      print

    if jsondatab['hits'][y].get('province'):
      province = '"'+jsondatab['hits'][y]['province'].encode("utf-8", "ignore")+'"'
      print
      print str(province)
      print

    if jsondatab['hits'][y].get('fullName'):
      fullName = '"'+jsondatab['hits'][y]['fullName'].encode("utf-8", "ignore")+'"'
      print
      print str(fullName)
      print

    if jsondatab['hits'][y].get('achievements'):
      achievements = '"'+str(jsondatab['hits'][y]['achievements']).encode("utf-8", "ignore")+'"'
      print
      print str(achievements)
      print

    if jsondatab['hits'][y].get('fullLocation'):
      fullLocation = '"'+jsondatab['hits'][y]['fullLocation'].encode("utf-8", "ignore")+'"'
      print
      print str(fullLocation)
      print

    if jsondatab['hits'][y].get('address'):
      address = '"'+jsondatab['hits'][y]['address'].encode("utf-8", "ignore")+'"'
      print
      print str(address)
      print

    if jsondatab['hits'][y].get('twitter'):
      twitter = "'"+jsondatab['hits'][y]['twitter'].encode("utf-8", "ignore")+"'"
      print
      print str(twitter)
      print

    if jsondatab['hits'][y].get('facebook'):
      facebook = "'"+jsondatab['hits'][y]['facebook'].encode("utf-8", "ignore")+"'"
      print
      print str(facebook)
      print

    if jsondatab['hits'][y].get('bio'):
      bio = '"'+jsondatab['hits'][y]['bio'].encode("utf-8", "ignore")+'"'
      print
      print str(bio)
      print

    if jsondatab['hits'][y].get('username'):
      username = "'"+jsondatab['hits'][y]['username'].encode("utf-8", "ignore")+"'"
      print
      print str(username)
      print

    if jsondatab['hits'][y].get('postalCode'):
      postalCode = "'"+jsondatab['hits'][y]['postalCode'].encode("utf-8", "ignore")+"'"
      print
      print str(postalCode)
      print

    if jsondatab['hits'][y].get('gender'):
      gender = "'"+jsondatab['hits'][y]['gender'].encode("utf-8", "ignore")+"'"
      print
      print str(gender)
      print

    if jsondatab['hits'][y].get('lastName'):
      lastName = "'"+jsondatab['hits'][y]['lastName'].encode("utf-8", "ignore")+"'"
      print
      print str(lastName)
      print

    if jsondatab['hits'][y].get('firstName'):
      firstName = "'"+jsondatab['hits'][y]['firstName'].encode("utf-8", "ignore")+"'"
      print
      print str(firstName)
      print

    if jsondatab['hits'][y].get('slug'):
      slug = "'"+jsondatab['hits'][y]['slug'].encode("utf-8", "ignore")+"'"
      print
      print str(slug)
      print


    if jsondatab['hits'][y].get('id'):
      lift_id = jsondatab['hits'][y]['id']
      print
      print str(lift_id)
      print

    if jsondatab['hits'][y].get('_id'):
      lift_id_2 = jsondatab['hits'][y]['_id']
      print
      print str(lift_id_2)
      print

    if jsondatab['hits'][y].get('__v'):
      lift__v = jsondatab['hits'][y]['__v']
      print
      print str(lift__v)
      print

    if jsondatab['hits'][y].get('reputation'):
      reputation = jsondatab['hits'][y]['reputation']
      print
      print str(reputation)
      print

    if jsondatab['hits'][y].get('helpfulReviewCount'):
      helpfulReviewCount = jsondatab['hits'][y]['helpfulReviewCount']
      print
      print str(helpfulReviewCount)
      print

    if jsondatab['hits'][y].get('reviewCount'):
      reviewCount = jsondatab['hits'][y]['reviewCount']
      print
      print str(reviewCount)
      print

    if jsondatab['hits'][y].get('age'):
      age = jsondatab['hits'][y]['age']
      print
      print str(age)
      print

    if jsondatab['hits'][y].get('verified'):
      verified = int(strtobool(str(jsondatab['hits'][y].get('verified'))) == 'true')
      print
      print str(verified)
      print

    if jsondatab['hits'][y].get('suspended'):
      suspended = int(strtobool(str(jsondatab['hits'][y].get('suspended'))) == 'true')
      print
      print str(suspended)
      print

    if jsondatab['hits'][y].get('banned'):
      banned = int(strtobool(str(jsondatab['hits'][y].get('banned'))) == 'true')
      print
      print str(banned)
      print

    if jsondatab['hits'][y].get('isAnonymous'):
      isAnonymous = int(strtobool(str(jsondatab['hits'][y].get('isAnonymous'))) == 'true')
      print
      print str(isAnonymous)
      print

    if jsondatab['hits'][y].get('usingCannabisSince'):
      try:
        ucs_pre = dateutil.parser.parse(jsondatab['hits'][y]['usingCannabisSince'])
        ucs = "'"+ucs_pre.strftime('%Y-%m-%d %H:%M:%S')+"'"
      except ValueError:
        ucs = "NULL"
      print
      print str(ucs)
      print

    if jsondatab['hits'][y].get('createdOn'):
      try:
        createdOn_pre = dateutil.parser.parse(jsondatab['hits'][y]['createdOn'])
        createdOn = "'"+createdOn_pre.strftime('%Y-%m-%d %H:%M:%S')+"'"
      except ValueError:
        createdOn = "NULL"
      print
      print str(createdOn)
      print

    if jsondatab['hits'][y].get('updatedOn'):
      try:
        updatedOn_pre = dateutil.parser.parse(jsondatab['hits'][y]['updatedOn'])
        updatedOn = "'"+updatedOn_pre.strftime('%Y-%m-%d %H:%M:%S')+"'"
      except ValueError:
        updatedOn = "NULL"
      print
      print str(updatedOn)
      print

    if jsondatab['hits'][y].get('profileCompletedOn'):
      try:
        profileCompletedOn_pre = dateutil.parser.parse(jsondatab['hits'][y]['profileCompletedOn'])
        profileCompletedOn = "'"+profileCompletedOn_pre.strftime('%Y-%m-%d %H:%M:%S')+"'"
      except ValueError:
        profileCompletedOn = "NULL"
      print
      print str(profileCompletedOn)
      print

    if jsondatab['hits'][y].get('joindate'):
      try:
        joindate_pre = dateutil.parser.parse(jsondatab['hits'][y]['joindate'])
        joindate = "'"+joindate_pre.strftime('%Y-%m-%d %H:%M:%S')+"'"
      except ValueError:
        joindate = "NULL"
      print
      print str(joindate)
      print

    if jsondatab['hits'][y].get('birthday'):
      try:
        birthday_pre = dateutil.parser.parse(jsondatab['hits'][y]['birthday'])
        birthday = "'"+birthday_pre.strftime('%Y-%m-%d %H:%M:%S')+"'"
      except ValueError:
        birthday = "NULL"
      print
      print str(birthday)
      print

    if jsondatab['hits'][y].get('lastOnline'):
      try:
        lastOnline_pre = dateutil.parser.parse(jsondatab['hits'][y]['lastOnline'])
        lastOnline = "'"+lastOnline_pre.strftime('%Y-%m-%d %H:%M:%S')+"'"
      except ValueError:
        lastOnline = "NULL"
      print
      print str(lastOnline)
      print



    if jsondatab['hits'][y].get('uploadedPicture'):
      uploadedPicture = jsondatab['hits'][y]['uploadedPicture']

      testfile = urllib.URLopener()

      path = urlparse.urlsplit(jsondatab['hits'][y].get('uploadedPicture')).path
      filename = posixpath.basename(path)
      print(filename)
      testfile.retrieve(jsondatab['hits'][y]['uploadedPicture'], "/tmp/lift-users/images/upload-"+filename)

    if jsondatab['hits'][y].get('gravatarPicture'):
      gravatarPicture = jsondatab['hits'][y]['gravatarPicture']

      testfile = urllib.URLopener()

      path = urlparse.urlsplit(jsondatab['hits'][y].get('gravatarPicture')).path
      filename = posixpath.basename(path)
      print(filename)
      testfile.retrieve(jsondatab['hits'][y]['gravatarPicture'], "/tmp/lift-users/images/grav-"+filename)

    if jsondatab['hits'][y].get('picture'):
      picture = jsondatab['hits'][y]['picture']

      testfile = urllib.URLopener()

      path = urlparse.urlsplit(jsondatab['hits'][y].get('picture')).path
      filename = posixpath.basename(path)
      print(filename)
      testfile.retrieve(jsondatab['hits'][y]['picture'], "/tmp/lift-users/images/pic-"+filename)

    sql1 = "INSERT INTO `lift-users` (lift_id, picture, slug, firstName, lastName, gender, postalCode, username, lift__v, lift_id_2, uploadedPicture, bio, birthday, facebook, twitter, gravatarPicture, achievements, fullLocation, address, city, province, fullName, usingCannabisSince, profileCompletedOn, cannabisExperience, updatedOn, createdOn, verified, suspended, banned, knownConditions, reputation, isAnonymous, helpfulReviewCount, reviewCount, role, joindate, lastOnline, age) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "  % (str (lift_id), str (picture), str (slug), str (firstName),str (lastName), str (gender), str (postalCode), str (username), str (lift__v), str (lift_id_2), str (uploadedPicture), str (bio), str (birthday), str (facebook), str (twitter), str (gravatarPicture), str (achievements), str (fullLocation), str (address), str (city), str (province), str (fullName), str (usingCannabisSince), str (profileCompletedOn), str (cannabisExperience), str (updatedOn), str (createdOn), str (verified), str (suspended), str (banned), str (knownConditions), str (reputation), str (isAnonymous), str (helpfulReviewCount), str (reviewCount), str (role), str (joindate), str (lastOnline), str (age))
    sql2 = "ON DUPLICATE KEY UPDATE picture=%s, slug=%s, firstName=%s, lastName=%s, gender=%s, postalCode=%s, username=%s, uploadedPicture=%s, bio=%s, birthday=%s, facebook=%s, twitter=%s, gravatarPicture=%s, achievements=%s, fullLocation=%s, address=%s, city=%s, province=%s, fullName=%s, usingCannabisSince=%s, profileCompletedOn=%s, cannabisExperience=%s, updatedOn=%s, verified=%s, suspended=%s, banned=%s, knownConditions=%s, reputation=%s, isAnonymous=%s, helpfulReviewCount=%s, reviewCount=%s, role=%s, lastOnline=%s, age=%s;" % (str(picture), str(slug), str(firstName), str(lastName), str(gender), str(postalCode), str(username), str(uploadedPicture), str(bio), str(birthday), str(facebook), str(twitter), str(gravatarPicture), str(achievements), str(fullLocation), str(address), str(city), str(province), str(fullName), str(usingCannabisSince), str(profileCompletedOn), str(cannabisExperience), str(updatedOn), str(verified), str(suspended), str(banned), str(knownConditions), str(reputation), str(isAnonymous), str(helpfulReviewCount), str(reviewCount), str(role), str(lastOnline), str(age))
    print(sql1+sql2)
    sqlquery = sql1+sql2
    cur.execute(sqlquery)
    db.commit()

  print
  print("-------------------------------------------------------------------------------------------------------------------------------------------------")

#print(jsondata['hits'][3]['reviews'])
#print(jsondata['hits'][3]['awards'])
#print(jsondata)

print("Pages: "+str(jsondatab['pages']))
print("Items: "+str(jsondatab['count']))
print("Page Number: "+str(jsondatab['page']))
