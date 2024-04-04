# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.datetime_utils import serialize_datetime
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ..commons.errors.access_denied_error import AccessDeniedError
from ..commons.errors.error import Error
from ..commons.errors.method_not_allowed_error import MethodNotAllowedError
from ..commons.errors.not_found_error import NotFoundError
from ..commons.errors.unauthorized_error import UnauthorizedError
from ..commons.types.score import Score
from .types.create_score_request import CreateScoreRequest
from .types.scores import Scores

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ScoreClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create(self, *, request: CreateScoreRequest) -> Score:
        """
        Create a score

        Parameters:
            - request: CreateScoreRequest.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/public/scores"
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Score, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise Error(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise AccessDeniedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowedError(
                pydantic.parse_obj_as(typing.Any, _response.json())
            )  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        user_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        from_timestamp: typing.Optional[dt.datetime] = None,
    ) -> Scores:
        """
        Get a list of scores

        Parameters:
            - page: typing.Optional[int].

            - limit: typing.Optional[int].

            - user_id: typing.Optional[str].

            - name: typing.Optional[str].

            - from_timestamp: typing.Optional[dt.datetime]. Retrieve only scores newer than this timestamp.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/public/scores"
            ),
            params=remove_none_from_dict(
                {
                    "page": page,
                    "limit": limit,
                    "userId": user_id,
                    "name": name,
                    "fromTimestamp": serialize_datetime(from_timestamp)
                    if from_timestamp is not None
                    else None,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Scores, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise Error(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise AccessDeniedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowedError(
                pydantic.parse_obj_as(typing.Any, _response.json())
            )  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_by_id(self, score_id: str) -> Score:
        """
        Get a score

        Parameters:
            - score_id: str. The unique langfuse identifier of a score
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/public/scores/{score_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Score, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise Error(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise AccessDeniedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowedError(
                pydantic.parse_obj_as(typing.Any, _response.json())
            )  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, score_id: str) -> None:
        """
        Delete a score

        Parameters:
            - score_id: str. The unique langfuse identifier of a score
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/public/scores/{score_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 400:
            raise Error(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise AccessDeniedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowedError(
                pydantic.parse_obj_as(typing.Any, _response.json())
            )  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncScoreClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create(self, *, request: CreateScoreRequest) -> Score:
        """
        Create a score

        Parameters:
            - request: CreateScoreRequest.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/public/scores"
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Score, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise Error(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise AccessDeniedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowedError(
                pydantic.parse_obj_as(typing.Any, _response.json())
            )  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        user_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        from_timestamp: typing.Optional[dt.datetime] = None,
    ) -> Scores:
        """
        Get a list of scores

        Parameters:
            - page: typing.Optional[int].

            - limit: typing.Optional[int].

            - user_id: typing.Optional[str].

            - name: typing.Optional[str].

            - from_timestamp: typing.Optional[dt.datetime]. Retrieve only scores newer than this timestamp.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", "api/public/scores"
            ),
            params=remove_none_from_dict(
                {
                    "page": page,
                    "limit": limit,
                    "userId": user_id,
                    "name": name,
                    "fromTimestamp": serialize_datetime(from_timestamp)
                    if from_timestamp is not None
                    else None,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Scores, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise Error(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise AccessDeniedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowedError(
                pydantic.parse_obj_as(typing.Any, _response.json())
            )  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_by_id(self, score_id: str) -> Score:
        """
        Get a score

        Parameters:
            - score_id: str. The unique langfuse identifier of a score
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/public/scores/{score_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Score, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise Error(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise AccessDeniedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowedError(
                pydantic.parse_obj_as(typing.Any, _response.json())
            )  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, score_id: str) -> None:
        """
        Delete a score

        Parameters:
            - score_id: str. The unique langfuse identifier of a score
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"api/public/scores/{score_id}",
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 400:
            raise Error(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise AccessDeniedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowedError(
                pydantic.parse_obj_as(typing.Any, _response.json())
            )  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
