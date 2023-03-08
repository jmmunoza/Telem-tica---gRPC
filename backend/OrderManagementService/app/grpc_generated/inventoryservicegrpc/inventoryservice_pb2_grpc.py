# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import app.grpc_generated.inventoryservicegrpc.inventoryservice_pb2 as inventoryservice__pb2


class InventoryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getAll = channel.unary_stream(
                '/InventoryService/getAll',
                request_serializer=inventoryservice__pb2.GetAllProductsRequest.SerializeToString,
                response_deserializer=inventoryservice__pb2.Product.FromString,
                )
        self.add = channel.unary_unary(
                '/InventoryService/add',
                request_serializer=inventoryservice__pb2.AddProductRequest.SerializeToString,
                response_deserializer=inventoryservice__pb2.Product.FromString,
                )
        self.get = channel.unary_unary(
                '/InventoryService/get',
                request_serializer=inventoryservice__pb2.GetProductRequest.SerializeToString,
                response_deserializer=inventoryservice__pb2.Product.FromString,
                )
        self.delete = channel.unary_unary(
                '/InventoryService/delete',
                request_serializer=inventoryservice__pb2.DeleteProductRequest.SerializeToString,
                response_deserializer=inventoryservice__pb2.ProductResponse.FromString,
                )
        self.update = channel.unary_unary(
                '/InventoryService/update',
                request_serializer=inventoryservice__pb2.Product.SerializeToString,
                response_deserializer=inventoryservice__pb2.ProductResponse.FromString,
                )


class InventoryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getAll(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def add(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InventoryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getAll': grpc.unary_stream_rpc_method_handler(
                    servicer.getAll,
                    request_deserializer=inventoryservice__pb2.GetAllProductsRequest.FromString,
                    response_serializer=inventoryservice__pb2.Product.SerializeToString,
            ),
            'add': grpc.unary_unary_rpc_method_handler(
                    servicer.add,
                    request_deserializer=inventoryservice__pb2.AddProductRequest.FromString,
                    response_serializer=inventoryservice__pb2.Product.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=inventoryservice__pb2.GetProductRequest.FromString,
                    response_serializer=inventoryservice__pb2.Product.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=inventoryservice__pb2.DeleteProductRequest.FromString,
                    response_serializer=inventoryservice__pb2.ProductResponse.SerializeToString,
            ),
            'update': grpc.unary_unary_rpc_method_handler(
                    servicer.update,
                    request_deserializer=inventoryservice__pb2.Product.FromString,
                    response_serializer=inventoryservice__pb2.ProductResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'InventoryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class InventoryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/InventoryService/getAll',
            inventoryservice__pb2.GetAllProductsRequest.SerializeToString,
            inventoryservice__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def add(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/add',
            inventoryservice__pb2.AddProductRequest.SerializeToString,
            inventoryservice__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/get',
            inventoryservice__pb2.GetProductRequest.SerializeToString,
            inventoryservice__pb2.Product.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/delete',
            inventoryservice__pb2.DeleteProductRequest.SerializeToString,
            inventoryservice__pb2.ProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/InventoryService/update',
            inventoryservice__pb2.Product.SerializeToString,
            inventoryservice__pb2.ProductResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
