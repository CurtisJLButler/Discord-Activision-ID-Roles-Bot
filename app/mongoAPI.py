import pymongo
import sys
import log

# Replace the placeholder data with your Atlas connection string. Be sure it includes
# a valid username and password! Note that in a production environment,
# you should not store your password in plain-text here.

try:
  client = pymongo.MongoClient("mongodb+srv://Discord-Bot:u46NUaqWhlAM4sSd@battle-buddies.pg7ih.mongodb.net/?retryWrites=true&w=majority&appName=Battle-Buddies")
  
# return a friendly error if a URI error is thrown 
except pymongo.errors.ConfigurationError:
  log.log_message("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
  sys.exit(1)
else:
   log.log_message("Succesfuly connected to MongoDB")

# use a database named "myDatabase"
db = client.battleBuddiesDB

# use a collection named "recipes"
my_collection = db["UserIDs"]



# drop the collection in case it already exists


# INSERT DOCUMENTS
#
# You can insert individual documents using collection.insert_one().
# In this example, we're going to create four documents and then 
# insert them all with insert_many().

def post(user, id):
    item = {user: id}
    try: 
        result = my_collection.insert_one(item)

    # return a friendly error if the operation fails
    except pymongo.errors.OperationFailure:
        log.log_message("An authentication error was received. Are you sure your database user is authorized to perform write operations?")
        sys.exit(1)
    else:
        log.log_message("I inserted %s documents." % (str(result.inserted_id)))

# # FIND DOCUMENTS
# #
# # Now that we have data in Atlas, we can read it. To retrieve all of
# # the data in a collection, we call find() with an empty filter. 

# result = my_collection.find()

# if result:    
#   for doc in result:
#     my_recipe = doc['name']
#     my_ingredient_count = len(doc['ingredients'])
#     my_prep_time = doc['prep_time']
#     print("%s has %x ingredients and takes %x minutes to make." %(my_recipe, my_ingredient_count, my_prep_time))
    
# else:
#   print("No documents found.")

# print("\n")

# # We can also find a single document. Let's find a document
# # that has the string "potato" in the ingredients list.
# my_doc = my_collection.find_one({"ingredients": "potato"})

# if my_doc is not None:
#   print("A recipe which uses potato:")
#   print(my_doc)
# else:
#   print("I didn't find any recipes that contain 'potato' as an ingredient.")
# print("\n")

# # UPDATE A DOCUMENT
# #
# # You can update a single document or multiple documents in a single call.
# # 
# # Here we update the prep_time value on the document we just found.
# #
# # Note the 'new=True' option: if omitted, find_one_and_update returns the
# # original document instead of the updated one.

# my_doc = my_collection.find_one_and_update({"ingredients": "potato"}, {"$set": { "prep_time": 72 }}, new=True)
# if my_doc is not None:
#   print("Here's the updated recipe:")
#   print(my_doc)
# else:
#   print("I didn't find any recipes that contain 'potato' as an ingredient.")
# print("\n")

# # DELETE DOCUMENTS
# #
# # As with other CRUD methods, you can delete a single document 
# # or all documents that match a specified filter. To delete all 
# # of the documents in a collection, pass an empty filter to 
# # the delete_many() method. In this example, we'll delete two of 
# # the recipes.
# #
# # The query filter passed to delete_many uses $or to look for documents
# # in which the "name" field is either "elotes" or "fried rice".

# my_result = my_collection.delete_many({ "$or": [{ "name": "elotes" }, { "name": "fried rice" }]})
# print("I deleted %x records." %(my_result.deleted_count))
# print("\n")