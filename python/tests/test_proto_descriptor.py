from google.protobuf import descriptor_pb2

from music.proto.gen import models_pb2


def test_get_albums_response_descriptor_references_album():
    file_descriptor_proto = descriptor_pb2.FileDescriptorProto()
    file_descriptor_proto.ParseFromString(models_pb2.DESCRIPTOR.serialized_pb)

    get_albums_response = next(
        message
        for message in file_descriptor_proto.message_type
        if message.name == "GetAlbumsResponse"
    )
    albums_field = next(
        field for field in get_albums_response.field if field.name == "albums"
    )

    assert albums_field.type_name == ".service.Album"
    assert (
        models_pb2.GetAlbumsResponse.DESCRIPTOR.fields_by_name["albums"]
        .message_type.full_name
        == "service.Album"
    )
