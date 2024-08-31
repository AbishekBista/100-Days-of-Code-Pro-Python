r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Conversations
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class DeliveryReceiptInstance(InstanceResource):

    class DeliveryStatus(object):
        READ = "read"
        FAILED = "failed"
        DELIVERED = "delivered"
        UNDELIVERED = "undelivered"
        SENT = "sent"

    """
    :ivar account_sid: The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for this participant.
    :ivar conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
    :ivar sid: A 34 character string that uniquely identifies this resource.
    :ivar message_sid: The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to
    :ivar channel_message_sid: A messaging channel-specific identifier for the message delivered to participant e.g. `SMxx` for SMS, `WAxx` for Whatsapp etc. 
    :ivar participant_sid: The unique ID of the participant the delivery receipt belongs to.
    :ivar status: 
    :ivar error_code: The message [delivery error code](https://www.twilio.com/docs/sms/api/message-resource#delivery-related-errors) for a `failed` status, 
    :ivar date_created: The date that this resource was created.
    :ivar date_updated: The date that this resource was last updated. `null` if the delivery receipt has not been updated.
    :ivar url: An absolute API resource URL for this delivery receipt.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        conversation_sid: str,
        message_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.conversation_sid: Optional[str] = payload.get("conversation_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.message_sid: Optional[str] = payload.get("message_sid")
        self.channel_message_sid: Optional[str] = payload.get("channel_message_sid")
        self.participant_sid: Optional[str] = payload.get("participant_sid")
        self.status: Optional["DeliveryReceiptInstance.DeliveryStatus"] = payload.get(
            "status"
        )
        self.error_code: Optional[int] = deserialize.integer(payload.get("error_code"))
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "conversation_sid": conversation_sid,
            "message_sid": message_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[DeliveryReceiptContext] = None

    @property
    def _proxy(self) -> "DeliveryReceiptContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DeliveryReceiptContext for this DeliveryReceiptInstance
        """
        if self._context is None:
            self._context = DeliveryReceiptContext(
                self._version,
                conversation_sid=self._solution["conversation_sid"],
                message_sid=self._solution["message_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "DeliveryReceiptInstance":
        """
        Fetch the DeliveryReceiptInstance


        :returns: The fetched DeliveryReceiptInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "DeliveryReceiptInstance":
        """
        Asynchronous coroutine to fetch the DeliveryReceiptInstance


        :returns: The fetched DeliveryReceiptInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.DeliveryReceiptInstance {}>".format(context)


class DeliveryReceiptContext(InstanceContext):

    def __init__(
        self, version: Version, conversation_sid: str, message_sid: str, sid: str
    ):
        """
        Initialize the DeliveryReceiptContext

        :param version: Version that contains the resource
        :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
        :param message_sid: The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to.
        :param sid: A 34 character string that uniquely identifies this resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "conversation_sid": conversation_sid,
            "message_sid": message_sid,
            "sid": sid,
        }
        self._uri = "/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts/{sid}".format(
            **self._solution
        )

    def fetch(self) -> DeliveryReceiptInstance:
        """
        Fetch the DeliveryReceiptInstance


        :returns: The fetched DeliveryReceiptInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return DeliveryReceiptInstance(
            self._version,
            payload,
            conversation_sid=self._solution["conversation_sid"],
            message_sid=self._solution["message_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> DeliveryReceiptInstance:
        """
        Asynchronous coroutine to fetch the DeliveryReceiptInstance


        :returns: The fetched DeliveryReceiptInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return DeliveryReceiptInstance(
            self._version,
            payload,
            conversation_sid=self._solution["conversation_sid"],
            message_sid=self._solution["message_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Conversations.V1.DeliveryReceiptContext {}>".format(context)


class DeliveryReceiptPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> DeliveryReceiptInstance:
        """
        Build an instance of DeliveryReceiptInstance

        :param payload: Payload response from the API
        """
        return DeliveryReceiptInstance(
            self._version,
            payload,
            conversation_sid=self._solution["conversation_sid"],
            message_sid=self._solution["message_sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.DeliveryReceiptPage>"


class DeliveryReceiptList(ListResource):

    def __init__(self, version: Version, conversation_sid: str, message_sid: str):
        """
        Initialize the DeliveryReceiptList

        :param version: Version that contains the resource
        :param conversation_sid: The unique ID of the [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) for this message.
        :param message_sid: The SID of the message within a [Conversation](https://www.twilio.com/docs/conversations/api/conversation-resource) the delivery receipt belongs to.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "conversation_sid": conversation_sid,
            "message_sid": message_sid,
        }
        self._uri = (
            "/Conversations/{conversation_sid}/Messages/{message_sid}/Receipts".format(
                **self._solution
            )
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[DeliveryReceiptInstance]:
        """
        Streams DeliveryReceiptInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[DeliveryReceiptInstance]:
        """
        Asynchronously streams DeliveryReceiptInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DeliveryReceiptInstance]:
        """
        Lists DeliveryReceiptInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DeliveryReceiptInstance]:
        """
        Asynchronously lists DeliveryReceiptInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> DeliveryReceiptPage:
        """
        Retrieve a single page of DeliveryReceiptInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of DeliveryReceiptInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return DeliveryReceiptPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> DeliveryReceiptPage:
        """
        Asynchronously retrieve a single page of DeliveryReceiptInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of DeliveryReceiptInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return DeliveryReceiptPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> DeliveryReceiptPage:
        """
        Retrieve a specific page of DeliveryReceiptInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of DeliveryReceiptInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return DeliveryReceiptPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> DeliveryReceiptPage:
        """
        Asynchronously retrieve a specific page of DeliveryReceiptInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of DeliveryReceiptInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return DeliveryReceiptPage(self._version, response, self._solution)

    def get(self, sid: str) -> DeliveryReceiptContext:
        """
        Constructs a DeliveryReceiptContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return DeliveryReceiptContext(
            self._version,
            conversation_sid=self._solution["conversation_sid"],
            message_sid=self._solution["message_sid"],
            sid=sid,
        )

    def __call__(self, sid: str) -> DeliveryReceiptContext:
        """
        Constructs a DeliveryReceiptContext

        :param sid: A 34 character string that uniquely identifies this resource.
        """
        return DeliveryReceiptContext(
            self._version,
            conversation_sid=self._solution["conversation_sid"],
            message_sid=self._solution["message_sid"],
            sid=sid,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Conversations.V1.DeliveryReceiptList>"
