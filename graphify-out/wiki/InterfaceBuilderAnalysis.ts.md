# InterfaceBuilderAnalysis.ts

> 37 nodes · cohesion 0.14

## Key Concepts

- **InterfaceBuilderAnalysis.ts** (93 connections) — `rea/src/artifacts/apple/InterfaceBuilderAnalysis.ts`
- **KeyedArchiveReader.ts** (75 connections) — `rea/src/artifacts/apple/KeyedArchiveReader.ts`
- **plistValue.ts** (39 connections) — `rea/src/domain/apple/plistValue.ts`
- **parsePlistBinary()** (24 connections) — `rea/src/native/parsers/plist.ts`
- **decodeKeyedArchiveBytes()** (22 connections) — `rea/src/artifacts/apple/KeyedArchiveReader.ts`
- **hasBinaryPlistSignature()** (20 connections) — `rea/src/domain/apple/appleArchiveFormat.ts`
- **projectPlistValue()** (18 connections) — `rea/src/domain/apple/plistValue.ts`
- **createPlistNumberProjection()** (11 connections) — `rea/src/domain/apple/plistNumbers.ts`
- **unknownDateLimitation()** (11 connections) — `rea/src/domain/apple/plistValue.ts`
- **projectKeyedArchive()** (10 connections) — `rea/src/domain/apple/keyedArchive.ts`
- **omittedPrototypeKeysLimitation()** (10 connections) — `rea/src/domain/propertyListKeys.ts`
- **decodePlist()** (9 connections) — `rea/src/artifacts/apple/InterfaceBuilderAnalysis.ts`
- **negativeZeroRealLimitation()** (9 connections) — `rea/src/domain/apple/plistValue.ts`
- **nonFiniteRealLimitation()** (9 connections) — `rea/src/domain/apple/plistValue.ts`
- **unknownScalarLimitation()** (9 connections) — `rea/src/domain/apple/plistValue.ts`
- **parseEntitlements()** (9 connections) — `rea/src/native/NativeMacOSProvider.ts`
- **finalizeHierarchyCoverage()** (8 connections) — `rea/src/artifacts/apple/InterfaceBuilderAnalysis.ts`
- **binaryDatePrecisionOverlapLimitation()** (7 connections) — `rea/src/domain/apple/plistValue.ts`
- **projectedScalarLimitations()** (7 connections) — `rea/src/native/parsers/plist.ts`
- **selectInterfaceBuilderCandidates()** (6 connections) — `rea/src/artifacts/apple/InterfaceBuilderAnalysis.ts`
- **retainBinaryPlistUidIdentity()** (6 connections) — `rea/src/artifacts/apple/PlistScalars.ts`
- **KeyedArchiveKindError** (5 connections) — `rea/src/domain/apple/keyedArchive.ts`
- **parseXmlWithinDecodeBudget()** (4 connections) — `rea/src/artifacts/apple/InterfaceBuilderAnalysis.ts`
- **uid()** (4 connections) — `rea/src/domain/apple/keyedArchive.ts`
- **negativeZeroReal()** (4 connections) — `rea/src/domain/apple/plistValue.ts`
- *... and 12 more nodes in this community*

## Relationships

- [propertyListKeys.ts](propertyListKeys.ts.md) (33 shared connections)
- [plist.ts](plist.ts.md) (29 shared connections)
- [PlistScalars.ts](PlistScalars.ts.md) (25 shared connections)
- [vitest](vitest.md) (22 shared connections)
- [NibArchive.ts](NibArchive.ts.md) (21 shared connections)
- [ArtifactReaderFailure](ArtifactReaderFailure.md) (20 shared connections)
- [AnalysisInputError](AnalysisInputError.md) (14 shared connections)
- [KeyedArchiveReader.test.ts](KeyedArchiveReader.test.ts.md) (13 shared connections)
- [BinaryTargetResolver.ts](BinaryTargetResolver.ts.md) (11 shared connections)
- [NativeMacOSProvider.ts](NativeMacOSProvider.ts.md) (11 shared connections)
- [interfaceBuilderKeyedArchive.ts](interfaceBuilderKeyedArchive.ts.md) (10 shared connections)
- [analysisErrorCore.ts](analysisErrorCore.ts.md) (9 shared connections)

## Source Files

- `rea/src/artifacts/apple/InterfaceBuilderAnalysis.ts`
- `rea/src/artifacts/apple/KeyedArchiveReader.ts`
- `rea/src/artifacts/apple/PlistScalars.ts`
- `rea/src/domain/apple/appleArchiveFormat.ts`
- `rea/src/domain/apple/keyedArchive.ts`
- `rea/src/domain/apple/plistNumbers.ts`
- `rea/src/domain/apple/plistValue.ts`
- `rea/src/domain/propertyListKeys.ts`
- `rea/src/native/NativeMacOSProvider.ts`
- `rea/src/native/parsers/plist.ts`

## Audit Trail

- EXTRACTED: 361 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*