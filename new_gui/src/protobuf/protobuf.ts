import protobuf from 'protobufjs';

const loadProto = async () => {
    return protobuf.load("messages.proto");
};

export const deserializeMessage = async (buffer: Uint8Array) => {
    const root = await loadProto();
    const WrapperMessage = root.lookupType("UIMessages.WrapperMessage");

    const message = WrapperMessage.decode(buffer);
    return WrapperMessage.toObject(message, {
        longs: String,
        enums: String,
        bytes: String,
    });
};
