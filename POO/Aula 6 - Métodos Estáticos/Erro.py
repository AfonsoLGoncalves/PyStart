class Error:

    @staticmethod
    def error_500() -> None:
        print("Internal Server Error!")

    @staticmethod
    def error_404() -> None:
        print("Not Found!")

Error.error_404()
Error.error_500()