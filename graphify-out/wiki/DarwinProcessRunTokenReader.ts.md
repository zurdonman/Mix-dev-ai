# DarwinProcessRunTokenReader.ts

> 103 nodes · cohesion 0.03

## Key Concepts

- **DarwinProcessRunTokenReader.ts** (86 connections) — `rea/src/process/DarwinProcessRunTokenReader.ts`
- **CommandRunner.ts** (75 connections) — `rea/src/native/CommandRunner.ts`
- **darwinProcessRunTokenReader.test.ts** (46 connections) — `rea/tests/boundary/process/darwinProcessRunTokenReader.test.ts`
- **DarwinProcessOwnershipInspectionError** (40 connections) — `rea/src/process/DarwinProcessRunTokenReader.ts`
- **NativeCommandFailure** (36 connections) — `rea/src/native/CommandRunner.ts`
- **darwinCompilerCleanup.test.ts** (32 connections) — `rea/tests/process-global/darwinCompilerCleanup.test.ts`
- **lldbPrelaunchCleanup.test.ts** (22 connections) — `rea/tests/boundary/providers/native/lldbPrelaunchCleanup.test.ts`
- **createDarwinProcessRunTokenReader()** (20 connections) — `rea/src/process/DarwinProcessRunTokenReader.ts`
- **processObservationCommandFinalization.test.ts** (19 connections) — `rea/tests/process-global/processObservationCommandFinalization.test.ts`
- **XcrunCommandRunner** (16 connections) — `rea/src/native/CommandRunner.ts`
- **ApktoolCommandOutput.ts** (12 connections) — `rea/src/apktool/ApktoolCommandOutput.ts`
- **nativeCommandTermination.test.ts** (12 connections) — `rea/tests/boundary/providers/native/nativeCommandTermination.test.ts`
- **captureProcess()** (10 connections) — `rea/src/native/CommandRunner.ts`
- **resolveXcrunTool()** (10 connections) — `rea/src/native/CommandRunner.ts`
- **abortReason()** (10 connections) — `rea/src/process/DarwinProcessRunTokenReader.ts`
- **.#runAfterCleanup()** (9 connections) — `rea/src/native/CommandRunner.ts`
- **nativeCommandResolver.test.ts** (9 connections) — `rea/tests/boundary/providers/native/nativeCommandResolver.test.ts`
- **failureCapture()** (7 connections) — `rea/src/native/CommandRunner.ts`
- **.run()** (7 connections) — `rea/src/native/CommandRunner.ts`
- **compilerInspectionError()** (6 connections) — `rea/src/process/DarwinProcessRunTokenReader.ts`
- **DarwinProcessRunTokenReader.timeout.test.ts** (6 connections) — `rea/src/process/DarwinProcessRunTokenReader.timeout.test.ts`
- **.#retainCleanupOwner()** (5 connections) — `rea/src/native/CommandRunner.ts`
- **translateCodeSignExitFailure()** (5 connections) — `rea/src/native/NativeMacOSProvider.ts`
- **compilerFailureFacts()** (5 connections) — `rea/src/process/DarwinProcessRunTokenReader.ts`
- **resolveSwiftcCompileTimeoutMs()** (5 connections) — `rea/src/process/DarwinProcessRunTokenReader.ts`
- *... and 78 more nodes in this community*

## Relationships

- [nativeInspection.ts](nativeInspection.ts.md) (36 shared connections)
- [ProviderProcess.ts](ProviderProcess.ts.md) (34 shared connections)
- [analysisErrorCore.ts](analysisErrorCore.ts.md) (33 shared connections)
- [vitest](vitest.md) (28 shared connections)
- [NativeMacOSProvider.ts](NativeMacOSProvider.ts.md) (21 shared connections)
- [GhidraLauncher.ts](GhidraLauncher.ts.md) (20 shared connections)
- [ok](ok.md) (20 shared connections)
- [AnalysisCancelledError](AnalysisCancelledError.md) (18 shared connections)
- [ProcessOwnership.ts](ProcessOwnership.ts.md) (15 shared connections)
- [AnalysisError](AnalysisError.md) (14 shared connections)
- [LldbCallTracer.ts](LldbCallTracer.ts.md) (14 shared connections)
- [ProcessCaptureLifecycle.ts](ProcessCaptureLifecycle.ts.md) (12 shared connections)

## Source Files

- `rea/src/apktool/ApktoolCommandOutput.ts`
- `rea/src/native/CommandRunner.ts`
- `rea/src/native/LldbCallTracer.ts`
- `rea/src/native/NativeMacOSProvider.ts`
- `rea/src/process/DarwinProcessRunTokenReader.timeout.test.ts`
- `rea/src/process/DarwinProcessRunTokenReader.ts`
- `rea/tests/boundary/process/darwinProcessRunTokenReader.test.ts`
- `rea/tests/boundary/providers/native/lldbPrelaunchCleanup.test.ts`
- `rea/tests/boundary/providers/native/nativeCommandResolver.test.ts`
- `rea/tests/boundary/providers/native/nativeCommandTermination.test.ts`
- `rea/tests/boundary/providers/native/nativeProvider.test.ts`
- `rea/tests/boundary/providers/native/plistSourceFormat.test.ts`
- `rea/tests/process-global/darwinCompilerCleanup.test.ts`
- `rea/tests/process-global/processObservationCommandFinalization.test.ts`

## Audit Trail

- EXTRACTED: 494 (97%)
- INFERRED: 16 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*