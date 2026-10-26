# NativeMachoInspection.ts

> 50 nodes · cohesion 0.09

## Key Concepts

- **NativeMachoInspection.ts** (73 connections) — `rea/src/native/NativeMachoInspection.ts`
- **inspectNativeMacho()** (25 connections) — `rea/src/native/NativeMachoInspection.ts`
- **NativeMachoCommandDiagnostics.ts** (17 connections) — `rea/src/native/NativeMachoCommandDiagnostics.ts`
- **normalizeMacho()** (15 connections) — `rea/src/native/NativeMachoInspection.ts`
- **dyldInfo.ts** (11 connections) — `rea/src/native/parsers/dyldInfo.ts`
- **parseDyldExports()** (7 connections) — `rea/src/native/parsers/dyldInfo.ts`
- **machoRuntimeSymbolName()** (6 connections) — `rea/src/domain/native/machoSymbolName.ts`
- **withoutEchoedPathHeader()** (6 connections) — `rea/src/native/parsers/echoedPath.ts`
- **conflictingUuidCommandEvidence()** (5 connections) — `rea/src/native/NativeMachoCommandDiagnostics.ts`
- **dyldFailureDiagnostics()** (5 connections) — `rea/src/native/NativeMachoCommandDiagnostics.ts`
- **isMissingUuidDyldFailure()** (5 connections) — `rea/src/native/NativeMachoCommandDiagnostics.ts`
- **nativeMachoCapturedOutput()** (5 connections) — `rea/src/native/NativeMachoCommandDiagnostics.ts`
- **unusableNativeCommandOutput()** (5 connections) — `rea/src/native/NativeMachoCommandDiagnostics.ts`
- **namesEveryExport()** (5 connections) — `rea/src/native/NativeMachoInspection.ts`
- **sliceOutput()** (5 connections) — `rea/src/native/NativeMachoInspection.ts`
- **machoSymbolName.ts** (4 connections) — `rea/src/domain/native/machoSymbolName.ts`
- **NativeCommandInvocation** (4 connections) — `rea/src/domain/native/nativeInspection.ts`
- **selectMachoArchitectureName()** (4 connections) — `rea/src/native/MachoArchitectureSelection.ts`
- **isUnbackedTextDyldFailure()** (4 connections) — `rea/src/native/NativeMachoCommandDiagnostics.ts`
- **parseDyldFileTypeRefusal()** (4 connections) — `rea/src/native/NativeMachoCommandDiagnostics.ts`
- **architectureLocations()** (4 connections) — `rea/src/native/NativeMachoInspection.ts`
- **toolArchitectureName()** (4 connections) — `rea/src/native/NativeMachoInspection.ts`
- **parseDyldImports()** (4 connections) — `rea/src/native/parsers/dyldInfo.ts`
- **echoedPath.ts** (4 connections) — `rea/src/native/parsers/echoedPath.ts`
- **machoSymbolName.test.ts** (3 connections) — `rea/src/domain/native/machoSymbolName.test.ts`
- *... and 25 more nodes in this community*

## Relationships

- [AnalysisError](AnalysisError.md) (8 shared connections)
- [nativeInspection.ts](nativeInspection.ts.md) (7 shared connections)
- [lipo.ts](lipo.ts.md) (7 shared connections)
- [NativeMacOSProvider.ts](NativeMacOSProvider.ts.md) (5 shared connections)
- [analysisErrorCore.ts](analysisErrorCore.ts.md) (5 shared connections)
- [AnalysisOutputError](AnalysisOutputError.md) (5 shared connections)
- [ok](ok.md) (5 shared connections)
- [vitest](vitest.md) (4 shared connections)
- [AnalysisProvider.ts](AnalysisProvider.ts.md) (4 shared connections)
- [managedReconstruction.ts](managedReconstruction.ts.md) (3 shared connections)
- [JsonValue](JsonValue.md) (3 shared connections)
- [compareUnicodeCodePoints](compareUnicodeCodePoints.md) (3 shared connections)

## Source Files

- `rea/src/domain/native/machoSymbolName.test.ts`
- `rea/src/domain/native/machoSymbolName.ts`
- `rea/src/domain/native/nativeInspection.ts`
- `rea/src/native/MachoArchitectureSelection.ts`
- `rea/src/native/NativeMachoCommandDiagnostics.ts`
- `rea/src/native/NativeMachoInspection.ts`
- `rea/src/native/parsers/dyldInfo.ts`
- `rea/src/native/parsers/echoedPath.test.ts`
- `rea/src/native/parsers/echoedPath.ts`

## Audit Trail

- EXTRACTED: 178 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*