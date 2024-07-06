// @generated by protoc-gen-es v1.10.0 with parameter "target=ts"
// @generated from file ui_messages.proto (package algo_commander, syntax proto3)
/* eslint-disable */
// @ts-nocheck

import type { BinaryReadOptions, FieldList, JsonReadOptions, JsonValue, PartialMessage, PlainMessage } from "@bufbuild/protobuf";
import { Message, proto3, protoInt64 } from "@bufbuild/protobuf";

/**
 * @generated from message algo_commander.RobotPosition
 */
export class RobotPosition extends Message<RobotPosition> {
  /**
   * @generated from field: int32 id = 1;
   */
  id = 0;

  /**
   * @generated from field: float pos_x = 2;
   */
  posX = 0;

  /**
   * @generated from field: float pos_y = 3;
   */
  posY = 0;

  /**
   * @generated from field: float angle = 4;
   */
  angle = 0;

  /**
   * @generated from field: bool blue_team = 5;
   */
  blueTeam = false;

  constructor(data?: PartialMessage<RobotPosition>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "algo_commander.RobotPosition";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "id", kind: "scalar", T: 5 /* ScalarType.INT32 */ },
    { no: 2, name: "pos_x", kind: "scalar", T: 2 /* ScalarType.FLOAT */ },
    { no: 3, name: "pos_y", kind: "scalar", T: 2 /* ScalarType.FLOAT */ },
    { no: 4, name: "angle", kind: "scalar", T: 2 /* ScalarType.FLOAT */ },
    { no: 5, name: "blue_team", kind: "scalar", T: 8 /* ScalarType.BOOL */ },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): RobotPosition {
    return new RobotPosition().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): RobotPosition {
    return new RobotPosition().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): RobotPosition {
    return new RobotPosition().fromJsonString(jsonString, options);
  }

  static equals(a: RobotPosition | PlainMessage<RobotPosition> | undefined, b: RobotPosition | PlainMessage<RobotPosition> | undefined): boolean {
    return proto3.util.equals(RobotPosition, a, b);
  }
}

/**
 * @generated from message algo_commander.Vector2f
 */
export class Vector2f extends Message<Vector2f> {
  /**
   * @generated from field: float x = 1;
   */
  x = 0;

  /**
   * @generated from field: float y = 2;
   */
  y = 0;

  constructor(data?: PartialMessage<Vector2f>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "algo_commander.Vector2f";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "x", kind: "scalar", T: 2 /* ScalarType.FLOAT */ },
    { no: 2, name: "y", kind: "scalar", T: 2 /* ScalarType.FLOAT */ },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): Vector2f {
    return new Vector2f().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): Vector2f {
    return new Vector2f().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): Vector2f {
    return new Vector2f().fromJsonString(jsonString, options);
  }

  static equals(a: Vector2f | PlainMessage<Vector2f> | undefined, b: Vector2f | PlainMessage<Vector2f> | undefined): boolean {
    return proto3.util.equals(Vector2f, a, b);
  }
}

/**
 * @generated from message algo_commander.Route
 */
export class Route extends Message<Route> {
  /**
   * @generated from field: repeated algo_commander.Vector2f points = 1;
   */
  points: Vector2f[] = [];

  /**
   * @generated from field: int32 robot_id = 2;
   */
  robotId = 0;

  /**
   * @generated from field: bool blue_team = 3;
   */
  blueTeam = false;

  constructor(data?: PartialMessage<Route>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "algo_commander.Route";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "points", kind: "message", T: Vector2f, repeated: true },
    { no: 2, name: "robot_id", kind: "scalar", T: 5 /* ScalarType.INT32 */ },
    { no: 3, name: "blue_team", kind: "scalar", T: 8 /* ScalarType.BOOL */ },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): Route {
    return new Route().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): Route {
    return new Route().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): Route {
    return new Route().fromJsonString(jsonString, options);
  }

  static equals(a: Route | PlainMessage<Route> | undefined, b: Route | PlainMessage<Route> | undefined): boolean {
    return proto3.util.equals(Route, a, b);
  }
}

/**
 * @generated from message algo_commander.RequestPath
 */
export class RequestPath extends Message<RequestPath> {
  /**
   * @generated from field: algo_commander.Vector2f from_point = 1;
   */
  fromPoint?: Vector2f;

  /**
   * @generated from field: algo_commander.Vector2f to_point = 2;
   */
  toPoint?: Vector2f;

  constructor(data?: PartialMessage<RequestPath>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "algo_commander.RequestPath";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "from_point", kind: "message", T: Vector2f },
    { no: 2, name: "to_point", kind: "message", T: Vector2f },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): RequestPath {
    return new RequestPath().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): RequestPath {
    return new RequestPath().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): RequestPath {
    return new RequestPath().fromJsonString(jsonString, options);
  }

  static equals(a: RequestPath | PlainMessage<RequestPath> | undefined, b: RequestPath | PlainMessage<RequestPath> | undefined): boolean {
    return proto3.util.equals(RequestPath, a, b);
  }
}

/**
 * @generated from message algo_commander.WrapperMessage
 */
export class WrapperMessage extends Message<WrapperMessage> {
  /**
   * @generated from field: int64 commonField = 1;
   */
  commonField = protoInt64.zero;

  /**
   * @generated from oneof algo_commander.WrapperMessage.msg
   */
  msg: {
    /**
     * @generated from field: algo_commander.RobotPosition robot_position = 2;
     */
    value: RobotPosition;
    case: "robotPosition";
  } | {
    /**
     * @generated from field: algo_commander.Route route = 3;
     */
    value: Route;
    case: "route";
  } | { case: undefined; value?: undefined } = { case: undefined };

  constructor(data?: PartialMessage<WrapperMessage>) {
    super();
    proto3.util.initPartial(data, this);
  }

  static readonly runtime: typeof proto3 = proto3;
  static readonly typeName = "algo_commander.WrapperMessage";
  static readonly fields: FieldList = proto3.util.newFieldList(() => [
    { no: 1, name: "commonField", kind: "scalar", T: 3 /* ScalarType.INT64 */ },
    { no: 2, name: "robot_position", kind: "message", T: RobotPosition, oneof: "msg" },
    { no: 3, name: "route", kind: "message", T: Route, oneof: "msg" },
  ]);

  static fromBinary(bytes: Uint8Array, options?: Partial<BinaryReadOptions>): WrapperMessage {
    return new WrapperMessage().fromBinary(bytes, options);
  }

  static fromJson(jsonValue: JsonValue, options?: Partial<JsonReadOptions>): WrapperMessage {
    return new WrapperMessage().fromJson(jsonValue, options);
  }

  static fromJsonString(jsonString: string, options?: Partial<JsonReadOptions>): WrapperMessage {
    return new WrapperMessage().fromJsonString(jsonString, options);
  }

  static equals(a: WrapperMessage | PlainMessage<WrapperMessage> | undefined, b: WrapperMessage | PlainMessage<WrapperMessage> | undefined): boolean {
    return proto3.util.equals(WrapperMessage, a, b);
  }
}

