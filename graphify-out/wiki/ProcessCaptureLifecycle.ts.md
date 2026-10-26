# ProcessCaptureLifecycle.ts

> 112 nodes · cohesion 0.05

## Key Concepts

- **ProcessCaptureLifecycle.ts** (160 connections) — `rea/src/process/capture/ProcessCaptureLifecycle.ts`
- **ProcessHarness.ts** (118 connections) — `rea/src/process/capture/ProcessHarness.ts`
- **ProcessHarness.test.ts** (41 connections) — `rea/src/process/capture/ProcessHarness.test.ts`
- **ProcessCaptureError** (37 connections) — `rea/src/process/capture/ProcessCaptureError.ts`
- **ProcessCaptureError.ts** (32 connections) — `rea/src/process/capture/ProcessCaptureError.ts`
- **captureProcessScenario()** (27 connections) — `rea/src/process/capture/ProcessHarness.ts`
- **ProcessCaptureResourceScope** (24 connections) — `rea/src/process/capture/ProcessCaptureLifecycle.ts`
- **ProcessCaptureError.test.ts** (22 connections) — `rea/src/process/capture/ProcessCaptureError.test.ts`
- **observeSelectedExecutable()** (19 connections) — `rea/src/process/capture/ProcessCaptureLifecycle.ts`
- **processCleanupRetryOwnership.test.ts** (19 connections) — `rea/tests/boundary/process/processCleanupRetryOwnership.test.ts`
- **resolveProcessResult()** (18 connections) — `rea/src/process/capture/ProcessCaptureLifecycle.ts`
- **prepareProcessCapture()** (17 connections) — `rea/src/process/capture/ProcessCaptureLifecycle.ts`
- **startCaptureRuntime()** (17 connections) — `rea/src/process/capture/ProcessHarness.ts`
- **ProcessCaptureCleanupReport** (16 connections) — `rea/src/domain/process/processCapture.ts`
- **monotonicProcessCaptureClock()** (16 connections) — `rea/src/process/capture/ProcessCaptureClock.ts`
- **normalizeCaptureFailure()** (15 connections) — `rea/src/process/capture/ProcessCaptureError.ts`
- **ProcessCaptureResourceOwner** (14 connections) — `rea/src/process/capture/ProcessCaptureLifecycle.ts`
- **ProcessCaptureProgress.ts** (14 connections) — `rea/src/process/capture/ProcessCaptureProgress.ts`
- **runProcessScenario()** (14 connections) — `rea/src/process/capture/ProcessHarness.ts`
- **processCaptureCancelled()** (13 connections) — `rea/src/process/capture/ProcessCaptureError.ts`
- **observeLaunchedExecutable()** (11 connections) — `rea/src/process/capture/ProcessCaptureLifecycle.ts`
- **completeCapture()** (11 connections) — `rea/src/process/capture/ProcessHarness.ts`
- **finishProcessRun()** (11 connections) — `rea/src/process/capture/ProcessHarness.ts`
- **observeSettlement()** (10 connections) — `rea/src/process/capture/ProcessCaptureLifecycle.ts`
- **assertNotCancelled()** (10 connections) — `rea/src/process/capture/ProcessScenarioRuntimeValidation.ts`
- *... and 87 more nodes in this community*

## Relationships

- [ProcessNormalization.ts](ProcessNormalization.ts.md) (92 shared connections)
- [processScenario.ts](processScenario.ts.md) (47 shared connections)
- [FilesystemSnapshot.ts](FilesystemSnapshot.ts.md) (45 shared connections)
- [ProcessOwnership.ts](ProcessOwnership.ts.md) (31 shared connections)
- [analysisErrorCore.ts](analysisErrorCore.ts.md) (26 shared connections)
- [zod](zod.md) (19 shared connections)
- [vitest](vitest.md) (17 shared connections)
- [processCapture.ts](processCapture.ts.md) (14 shared connections)
- [ProcessCaptureLifecycle.test.ts](ProcessCaptureLifecycle.test.ts.md) (13 shared connections)
- [processCaptureLifecycle.test.ts](processCaptureLifecycle.test.ts_2.md) (13 shared connections)
- [DarwinProcessRunTokenReader.ts](DarwinProcessRunTokenReader.ts.md) (12 shared connections)
- [createServer.ts](createServer.ts.md) (12 shared connections)

## Source Files

- `rea/src/domain/process/processCapture.ts`
- `rea/src/process/ProcessOwnership.ts`
- `rea/src/process/ProcessOwnershipProcessTree.ts`
- `rea/src/process/capture/ProcessCaptureClock.ts`
- `rea/src/process/capture/ProcessCaptureEnvironment.ts`
- `rea/src/process/capture/ProcessCaptureError.test.ts`
- `rea/src/process/capture/ProcessCaptureError.ts`
- `rea/src/process/capture/ProcessCaptureLifecycle.ts`
- `rea/src/process/capture/ProcessCaptureProgress.test.ts`
- `rea/src/process/capture/ProcessCaptureProgress.ts`
- `rea/src/process/capture/ProcessHarness.test.ts`
- `rea/src/process/capture/ProcessHarness.ts`
- `rea/src/process/capture/ProcessScenarioRuntimeValidation.ts`
- `rea/src/process/capture/ProcessTerminalObservation.ts`
- `rea/tests/boundary/process/processCaptureCallerReason.test.ts`
- `rea/tests/boundary/process/processCleanupRetryOwnership.test.ts`
- `rea/tests/boundary/process/processHostIdentity.test.ts`

## Audit Trail

- EXTRACTED: 699 (97%)
- INFERRED: 20 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*