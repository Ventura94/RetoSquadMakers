from fastapi import HTTPException, status


class NotFound(HTTPException):
    def __init__(self, detail: any = 'Not found', headers: dict[str, any] | None = None):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
        self.headers = headers


class ValidationError(HTTPException):
    def __init__(self, detail: any = 'Invalid input', headers: dict[str, any] | None = None, ):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
        self.headers = headers
