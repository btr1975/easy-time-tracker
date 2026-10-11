"""
NeoSQLLite client
"""

from typing import Optional, Any
from neosqlite import Connection
from neosqlite.collection import Collection, Cursor, AggregationCursor
from neosqlite.collection import InsertOneResult, DeleteResult, UpdateResult
from easy_time_tracker.util.schemas import Person, get_current_datetime


class NeoSQLiteClient:  # pylint: disable=too-many-public-methods
    """NeoSQLite client

    :param neosqlite_connection: The neosqlite connection

    :returns: Nothing it creates a client
    """

    def __init__(self, neosqlite_connection: Connection) -> None:
        self._client = neosqlite_connection

        self._database_name = "easy_time_tracker"
        self._projects_collection = "projects"
        self._people_collection = "people"

    def get_database(self) -> Connection:
        """Method to get the database

        :returns: The database
        """
        return self._client.get_database(name=self._database_name)

    def close_client(self) -> None:
        """Method to close the pymongo client

        :returns: Nothing it closes the client
        """
        self._client.close()

    def get_collections_list(self) -> list[dict[str, Any]]:
        """Method to get a list of collections in the database

        :returns: The command cursor
        """
        return self.get_database().list_collections()

    def get_current_collections_names(self) -> list[str]:
        """Get the names of the current collections in the database

        :returns: The current collections names
        """
        names = []
        for collection in self.get_collections_list():
            names.append(collection["name"])

        return names

    def get_collection(self, collection_name: str) -> Collection:
        """Method to get a collection

        :param collection_name: The name of the collection

        :returns: The collection
        """
        if collection_name not in self.get_current_collections_names():
            self.get_database().create_collection(name=collection_name)

        return self.get_database().get_collection(name=collection_name)

    def create_document(self, collection_name: str, document_data: dict) -> InsertOneResult:
        """Method to create a document in the collection

        :param collection_name: The name of the collection
        :param document_data: The data for the new document

        :returns: The ID of the new document
        """
        return self.get_collection(collection_name=collection_name).insert_one(document=document_data)

    def delete_one_document(self, collection_name: str, data_filter: dict) -> DeleteResult:
        """Method to delete one document from the collection

        :param collection_name: The name of the collection
        :param data_filter: The filter data

        :returns: The response from neosqlite

        :raises ValueError: If collection name is not set in class
        """
        return self.get_collection(collection_name=collection_name).delete_one(filter=data_filter)

    def find_documents(
        self,
        collection_name: str,
        data_filter: Optional[dict] = None,
        projection: Optional[dict] = None,
        skip: Optional[int] = 0,
        limit: Optional[int] = 0,
    ) -> Cursor:
        """Method to find documents in the collection

        :param collection_name: The name of the collection
        :param data_filter: The filter data
        :param projection: The neosqlite projection
        :param skip: The number of documents to skip
        :param limit: The number of documents to limit

        :returns: The response from neosqlite

        :raises ValueError: If collection name is not set in class
        """
        return self.get_collection(collection_name=collection_name).find(
            filter=data_filter, projection=projection, skip=skip, limit=limit
        )

    def find_one_document(
        self, collection_name: str, data_filter: Optional[dict] = None, projection: Optional[dict] = None
    ) -> dict[str, Any] | None:
        """Method to find one document in the collection

        :param collection_name: The name of the collection
        :param data_filter: The filter data
        :param projection: The neosqlite projection

        :returns: The response from neosqlite

        :raises ValueError: If collection name is not set in class
        """
        return self.get_collection(collection_name=collection_name).find_one(filter=data_filter, projection=projection)

    def update_one_document(
        self, collection_name: str, data_filter: dict, update_data: dict, upsert: bool = True
    ) -> UpdateResult:
        """Method to find one document in the collection

        :param collection_name: The name of the collection
        :param data_filter: The filter data
        :param update_data: The data to update
        :param upsert: Set False to not use upsert

        :returns: The response from neosqlite

        :raises ValueError: If collection name is not set in class
        """
        return self.get_collection(collection_name=collection_name).update_one(
            filter=data_filter, update=update_data, upsert=upsert
        )

    def name_exists(self, collection_name: str, name: str) -> bool:
        """Method to check if a name in a document exists

        :param collection_name: The name of the collection
        :param name: The name

        :returns: If exists True, else False
        """
        response = self.find_one_document(
            collection_name=collection_name, data_filter={"name": name}, projection={"name": True, "_id": False}
        )

        if response:
            return True

        return False

    def get_document_count(self, collection_name: str, data_filter: Optional[dict] = None) -> int:
        """Method to get count of records in a collection

        :param collection_name: The name of the collection
        :param data_filter: The filter data

        :returns: The count of documents

        :raises ValueError: If collection name is not set in class
        """
        if not data_filter:
            return self.get_collection(collection_name=collection_name).count_documents({})

        return self.get_collection(collection_name=collection_name).count_documents(filter=data_filter)

    def aggregation(self, collection_name: str, pipeline: list) -> AggregationCursor:
        """Method to run an aggregation pipeline

        :param collection_name: The name of the collection
        :param pipeline: The aggregation pipeline

        :returns: The response from neosqlite
        """
        return self.get_collection(collection_name=collection_name).aggregate(pipeline=pipeline)

    def create_person(self, document: Person) -> InsertOneResult:
        """Create a new person in the people collection

        :param document: The document to create

        :returns: The response from neosqlite

        :raises TypeError: If the document is not a Person
        """
        if not isinstance(document, Person):
            raise TypeError(f"'document' must be of type Person, not {type(document)}")

        return self.get_collection(collection_name=self._people_collection).insert_one(document=document.model_dump())

    def get_people(
        self,
        data_filter: Optional[dict] = None,
        projection: Optional[dict] = None,
        skip: Optional[int] = 0,
        limit: Optional[int] = 0,
    ) -> Cursor:
        """Get people in the people collection

        :returns: The cursor
        """
        this_projection = {"_id": False}

        if projection:
            this_projection.update(projection)

        return self.find_documents(
            collection_name=self._people_collection,
            data_filter=data_filter,
            projection=this_projection,
            skip=skip,
            limit=limit,
        )

    def update_person(
        self,
        data_filter: dict[Any, Any],
        update_data: dict[Any, Any],
    ) -> UpdateResult:
        """Update a person in the people collection

        :returns: The cursor
        """
        this_update = {"modified": get_current_datetime()}
        this_update.update(update_data)

        return self.update_one_document(
            collection_name=self._people_collection,
            data_filter=data_filter,
            update_data={"$set": this_update},
            upsert=True,
        )
