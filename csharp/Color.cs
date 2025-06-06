// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: common/v1/color.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Messages.Common.V1 {

  /// <summary>Holder for reflection information generated from common/v1/color.proto</summary>
  public static partial class ColorReflection {

    #region Descriptor
    /// <summary>File descriptor for common/v1/color.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static ColorReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "ChVjb21tb24vdjEvY29sb3IucHJvdG8SCWNvbW1vbi52MSJZCgVDb2xvchIQ",
            "CgNyZWQYASABKAJSA3JlZBIUCgVncmVlbhgCIAEoAlIFZ3JlZW4SEgoEYmx1",
            "ZRgDIAEoAlIEYmx1ZRIUCgVhbHBoYRgEIAEoAlIFYWxwaGFCogEKDWNvbS5j",
            "b21tb24udjFCCkNvbG9yUHJvdG9QAVo3Z2l0aHViLmNvbS9jb2JvdGFyL3By",
            "b3RvY29sL21lc3NhZ2VzL2NvbW1vbi92MTtjb21tb252MaICA0NYWKoCEk1l",
            "c3NhZ2VzLkNvbW1vbi5WMcoCCUNvbW1vblxWMeICFUNvbW1vblxWMVxHUEJN",
            "ZXRhZGF0YeoCCkNvbW1vbjo6VjFiBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Messages.Common.V1.Color), global::Messages.Common.V1.Color.Parser, new[]{ "Red", "Green", "Blue", "Alpha" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  /// <summary>
  /// Represents a color. Where (1, 1, 1, 1) is solid white, (1, 0, 0, 0.5) is half transparent red, and so on.
  /// </summary>
  [global::System.Diagnostics.DebuggerDisplayAttribute("{ToString(),nq}")]
  public sealed partial class Color : pb::IMessage<Color>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<Color> _parser = new pb::MessageParser<Color>(() => new Color());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<Color> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Messages.Common.V1.ColorReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Color() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Color(Color other) : this() {
      red_ = other.red_;
      green_ = other.green_;
      blue_ = other.blue_;
      alpha_ = other.alpha_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public Color Clone() {
      return new Color(this);
    }

    /// <summary>Field number for the "red" field.</summary>
    public const int RedFieldNumber = 1;
    private float red_;
    /// <summary>
    /// Ranging from [0:1]
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public float Red {
      get { return red_; }
      set {
        red_ = value;
      }
    }

    /// <summary>Field number for the "green" field.</summary>
    public const int GreenFieldNumber = 2;
    private float green_;
    /// <summary>
    /// Ranging from [0:1]
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public float Green {
      get { return green_; }
      set {
        green_ = value;
      }
    }

    /// <summary>Field number for the "blue" field.</summary>
    public const int BlueFieldNumber = 3;
    private float blue_;
    /// <summary>
    /// Ranging from [0:1]
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public float Blue {
      get { return blue_; }
      set {
        blue_ = value;
      }
    }

    /// <summary>Field number for the "alpha" field.</summary>
    public const int AlphaFieldNumber = 4;
    private float alpha_;
    /// <summary>
    /// Ranging from [0:1] --> [transparent : opaque]
    /// </summary>
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public float Alpha {
      get { return alpha_; }
      set {
        alpha_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as Color);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(Color other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.Equals(Red, other.Red)) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.Equals(Green, other.Green)) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.Equals(Blue, other.Blue)) return false;
      if (!pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.Equals(Alpha, other.Alpha)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (Red != 0F) hash ^= pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.GetHashCode(Red);
      if (Green != 0F) hash ^= pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.GetHashCode(Green);
      if (Blue != 0F) hash ^= pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.GetHashCode(Blue);
      if (Alpha != 0F) hash ^= pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.GetHashCode(Alpha);
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (Red != 0F) {
        output.WriteRawTag(13);
        output.WriteFloat(Red);
      }
      if (Green != 0F) {
        output.WriteRawTag(21);
        output.WriteFloat(Green);
      }
      if (Blue != 0F) {
        output.WriteRawTag(29);
        output.WriteFloat(Blue);
      }
      if (Alpha != 0F) {
        output.WriteRawTag(37);
        output.WriteFloat(Alpha);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (Red != 0F) {
        output.WriteRawTag(13);
        output.WriteFloat(Red);
      }
      if (Green != 0F) {
        output.WriteRawTag(21);
        output.WriteFloat(Green);
      }
      if (Blue != 0F) {
        output.WriteRawTag(29);
        output.WriteFloat(Blue);
      }
      if (Alpha != 0F) {
        output.WriteRawTag(37);
        output.WriteFloat(Alpha);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (Red != 0F) {
        size += 1 + 4;
      }
      if (Green != 0F) {
        size += 1 + 4;
      }
      if (Blue != 0F) {
        size += 1 + 4;
      }
      if (Alpha != 0F) {
        size += 1 + 4;
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(Color other) {
      if (other == null) {
        return;
      }
      if (other.Red != 0F) {
        Red = other.Red;
      }
      if (other.Green != 0F) {
        Green = other.Green;
      }
      if (other.Blue != 0F) {
        Blue = other.Blue;
      }
      if (other.Alpha != 0F) {
        Alpha = other.Alpha;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
      if ((tag & 7) == 4) {
        // Abort on any end group tag.
        return;
      }
      switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 13: {
            Red = input.ReadFloat();
            break;
          }
          case 21: {
            Green = input.ReadFloat();
            break;
          }
          case 29: {
            Blue = input.ReadFloat();
            break;
          }
          case 37: {
            Alpha = input.ReadFloat();
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
      if ((tag & 7) == 4) {
        // Abort on any end group tag.
        return;
      }
      switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 13: {
            Red = input.ReadFloat();
            break;
          }
          case 21: {
            Green = input.ReadFloat();
            break;
          }
          case 29: {
            Blue = input.ReadFloat();
            break;
          }
          case 37: {
            Alpha = input.ReadFloat();
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code
