# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from Browser.generated import playwright_pb2 as playwright__pb2


class PlaywrightStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Screenshot = channel.unary_unary(
                '/Playwright/Screenshot',
                request_serializer=playwright__pb2.screenshotRequest.SerializeToString,
                response_deserializer=playwright__pb2.Response.Empty.FromString,
                )
        self.OpenBrowser = channel.unary_unary(
                '/Playwright/OpenBrowser',
                request_serializer=playwright__pb2.openBrowserRequest.SerializeToString,
                response_deserializer=playwright__pb2.Response.Empty.FromString,
                )
        self.CloseBrowser = channel.unary_unary(
                '/Playwright/CloseBrowser',
                request_serializer=playwright__pb2.Empty.SerializeToString,
                response_deserializer=playwright__pb2.Response.Empty.FromString,
                )
        self.GoTo = channel.unary_unary(
                '/Playwright/GoTo',
                request_serializer=playwright__pb2.goToRequest.SerializeToString,
                response_deserializer=playwright__pb2.Response.Empty.FromString,
                )
        self.GetTitle = channel.unary_unary(
                '/Playwright/GetTitle',
                request_serializer=playwright__pb2.Empty.SerializeToString,
                response_deserializer=playwright__pb2.Response.String.FromString,
                )
        self.InputText = channel.unary_unary(
                '/Playwright/InputText',
                request_serializer=playwright__pb2.inputTextRequest.SerializeToString,
                response_deserializer=playwright__pb2.Response.Empty.FromString,
                )
        self.GetDomProperty = channel.unary_unary(
                '/Playwright/GetDomProperty',
                request_serializer=playwright__pb2.getDomPropertyRequest.SerializeToString,
                response_deserializer=playwright__pb2.Response.String.FromString,
                )
        self.GetTextContent = channel.unary_unary(
                '/Playwright/GetTextContent',
                request_serializer=playwright__pb2.selectorRequest.SerializeToString,
                response_deserializer=playwright__pb2.Response.String.FromString,
                )
        self.GetUrl = channel.unary_unary(
                '/Playwright/GetUrl',
                request_serializer=playwright__pb2.Empty.SerializeToString,
                response_deserializer=playwright__pb2.Response.String.FromString,
                )
        self.ClickButton = channel.unary_unary(
                '/Playwright/ClickButton',
                request_serializer=playwright__pb2.selectorRequest.SerializeToString,
                response_deserializer=playwright__pb2.Response.Empty.FromString,
                )
        self.CheckCheckbox = channel.unary_unary(
                '/Playwright/CheckCheckbox',
                request_serializer=playwright__pb2.selectorRequest.SerializeToString,
                response_deserializer=playwright__pb2.Response.Empty.FromString,
                )
        self.UncheckCheckbox = channel.unary_unary(
                '/Playwright/UncheckCheckbox',
                request_serializer=playwright__pb2.selectorRequest.SerializeToString,
                response_deserializer=playwright__pb2.Response.Empty.FromString,
                )
        self.Health = channel.unary_unary(
                '/Playwright/Health',
                request_serializer=playwright__pb2.Empty.SerializeToString,
                response_deserializer=playwright__pb2.Response.String.FromString,
                )


class PlaywrightServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Screenshot(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def OpenBrowser(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseBrowser(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GoTo(self, request, context):
        """Opens the url in currently open Playwright page 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTitle(self, request, context):
        """Gets title of currently open Playwright page 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InputText(self, request, context):
        """Wraps playwrights page.fill to input text into input specified with selector 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDomProperty(self, request, context):
        """Gets the DOM property 'property' of selector specified element 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTextContent(self, request, context):
        """Wraps playwrights page.textContent, returns textcontent of element by selector 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUrl(self, request, context):
        """*Returns current playwright page url
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClickButton(self, request, context):
        """Clicks button specified by selector 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckCheckbox(self, request, context):
        """Checks checkbox specified by selector 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UncheckCheckbox(self, request, context):
        """Unchecks checkbox specified by selector 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Health(self, request, context):
        """Health check endpoint for the service 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PlaywrightServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Screenshot': grpc.unary_unary_rpc_method_handler(
                    servicer.Screenshot,
                    request_deserializer=playwright__pb2.screenshotRequest.FromString,
                    response_serializer=playwright__pb2.Response.Empty.SerializeToString,
            ),
            'OpenBrowser': grpc.unary_unary_rpc_method_handler(
                    servicer.OpenBrowser,
                    request_deserializer=playwright__pb2.openBrowserRequest.FromString,
                    response_serializer=playwright__pb2.Response.Empty.SerializeToString,
            ),
            'CloseBrowser': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseBrowser,
                    request_deserializer=playwright__pb2.Empty.FromString,
                    response_serializer=playwright__pb2.Response.Empty.SerializeToString,
            ),
            'GoTo': grpc.unary_unary_rpc_method_handler(
                    servicer.GoTo,
                    request_deserializer=playwright__pb2.goToRequest.FromString,
                    response_serializer=playwright__pb2.Response.Empty.SerializeToString,
            ),
            'GetTitle': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTitle,
                    request_deserializer=playwright__pb2.Empty.FromString,
                    response_serializer=playwright__pb2.Response.String.SerializeToString,
            ),
            'InputText': grpc.unary_unary_rpc_method_handler(
                    servicer.InputText,
                    request_deserializer=playwright__pb2.inputTextRequest.FromString,
                    response_serializer=playwright__pb2.Response.Empty.SerializeToString,
            ),
            'GetDomProperty': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDomProperty,
                    request_deserializer=playwright__pb2.getDomPropertyRequest.FromString,
                    response_serializer=playwright__pb2.Response.String.SerializeToString,
            ),
            'GetTextContent': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTextContent,
                    request_deserializer=playwright__pb2.selectorRequest.FromString,
                    response_serializer=playwright__pb2.Response.String.SerializeToString,
            ),
            'GetUrl': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUrl,
                    request_deserializer=playwright__pb2.Empty.FromString,
                    response_serializer=playwright__pb2.Response.String.SerializeToString,
            ),
            'ClickButton': grpc.unary_unary_rpc_method_handler(
                    servicer.ClickButton,
                    request_deserializer=playwright__pb2.selectorRequest.FromString,
                    response_serializer=playwright__pb2.Response.Empty.SerializeToString,
            ),
            'CheckCheckbox': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckCheckbox,
                    request_deserializer=playwright__pb2.selectorRequest.FromString,
                    response_serializer=playwright__pb2.Response.Empty.SerializeToString,
            ),
            'UncheckCheckbox': grpc.unary_unary_rpc_method_handler(
                    servicer.UncheckCheckbox,
                    request_deserializer=playwright__pb2.selectorRequest.FromString,
                    response_serializer=playwright__pb2.Response.Empty.SerializeToString,
            ),
            'Health': grpc.unary_unary_rpc_method_handler(
                    servicer.Health,
                    request_deserializer=playwright__pb2.Empty.FromString,
                    response_serializer=playwright__pb2.Response.String.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Playwright', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Playwright(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Screenshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Playwright/Screenshot',
            playwright__pb2.screenshotRequest.SerializeToString,
            playwright__pb2.Response.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def OpenBrowser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Playwright/OpenBrowser',
            playwright__pb2.openBrowserRequest.SerializeToString,
            playwright__pb2.Response.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseBrowser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Playwright/CloseBrowser',
            playwright__pb2.Empty.SerializeToString,
            playwright__pb2.Response.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GoTo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Playwright/GoTo',
            playwright__pb2.goToRequest.SerializeToString,
            playwright__pb2.Response.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTitle(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Playwright/GetTitle',
            playwright__pb2.Empty.SerializeToString,
            playwright__pb2.Response.String.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InputText(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Playwright/InputText',
            playwright__pb2.inputTextRequest.SerializeToString,
            playwright__pb2.Response.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDomProperty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Playwright/GetDomProperty',
            playwright__pb2.getDomPropertyRequest.SerializeToString,
            playwright__pb2.Response.String.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTextContent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Playwright/GetTextContent',
            playwright__pb2.selectorRequest.SerializeToString,
            playwright__pb2.Response.String.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUrl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Playwright/GetUrl',
            playwright__pb2.Empty.SerializeToString,
            playwright__pb2.Response.String.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClickButton(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Playwright/ClickButton',
            playwright__pb2.selectorRequest.SerializeToString,
            playwright__pb2.Response.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckCheckbox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Playwright/CheckCheckbox',
            playwright__pb2.selectorRequest.SerializeToString,
            playwright__pb2.Response.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UncheckCheckbox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Playwright/UncheckCheckbox',
            playwright__pb2.selectorRequest.SerializeToString,
            playwright__pb2.Response.Empty.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Health(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Playwright/Health',
            playwright__pb2.Empty.SerializeToString,
            playwright__pb2.Response.String.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
