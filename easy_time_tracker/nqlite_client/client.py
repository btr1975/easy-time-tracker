"""
NeoSQLLite client
"""

from typing import Optional, Any
from neosqlite import Connection
from neosqlite.collection import Collection, Cursor, AggregationCursor
from neosqlite.collection import InsertOneResult, DeleteResult, UpdateResult


class NeoSQLiteClient:  # pylint: disable=too-many-public-methods
    """NeoSQLite client

    :param neosqlite_connection: The neosqlite connection

    :returns: Nothing it creates a client
    """

    def __init__(self, neosqlite_connection: Connection) -> None:
        self._client = neosqlite_connection

        self._database_name = "easy_time_tracker"

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

    def get_collection(self, collection_name: str) -> Collection:
        """Method to get a collection

        :param collection_name: The name of the collection

        :returns: The collection
        """
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

        :returns: The response from mongo

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
        :param projection: The mongo projection
        :param skip: The number of documents to skip
        :param limit: The number of documents to limit

        :returns: The response from mongo

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
        :param projection: The mongo projection

        :returns: The response from mongo

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

        :returns: The response from mongo

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

        :returns: The response from mongo
        """
        return self.get_collection(collection_name=collection_name).aggregate(pipeline=pipeline)
