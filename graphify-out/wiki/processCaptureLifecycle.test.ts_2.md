# processCaptureLifecycle.test.ts

> 38 nodes · cohesion 0.08

## Key Concepts

- **processCaptureLifecycle.test.ts** (50 connections) — `rea/tests/boundary/process/processCaptureLifecycle.test.ts`
- **processFinalization.test.ts** (45 connections) — `rea/tests/acceptance/process/processFinalization.test.ts`
- **hostCleanup.ts** (11 connections) — `rea/tests/support/hostCleanup.ts`
- **captureViaMcp()** (7 connections) — `rea/tests/acceptance/process/processFinalization.test.ts`
- **expectSerializedUnverifiedHostCleanup()** (6 connections) — `rea/tests/support/hostCleanup.ts`
- **captureViaCli()** (5 connections) — `rea/tests/acceptance/process/processFinalization.test.ts`
- **FinalizationHost** (4 connections) — `rea/src/process/capture/ProcessHarness.ts`
- **waitFor()** (4 connections) — `rea/tests/acceptance/process/processFinalization.test.ts`
- **expectUnverifiedHostCleanup()** (4 connections) — `rea/tests/support/hostCleanup.ts`
- **completedCaptureFromOutcome()** (3 connections) — `rea/tests/acceptance/process/processFinalization.test.ts`
- **fixturePid()** (3 connections) — `rea/tests/acceptance/process/processFinalization.test.ts`
- **waitForFinalization()** (3 connections) — `rea/tests/acceptance/process/processFinalization.test.ts`
- **captureFinalizationFixture()** (3 connections) — `rea/tests/boundary/process/processCaptureLifecycle.test.ts`
- **processState()** (3 connections) — `rea/tests/boundary/process/processCaptureLifecycle.test.ts`
- **waitForProcessExit()** (3 connections) — `rea/tests/boundary/process/processCaptureLifecycle.test.ts`
- **expectHostCleanupReport()** (3 connections) — `rea/tests/support/hostCleanup.ts`
- **isSerializedCleanupReport()** (3 connections) — `rea/tests/support/hostCleanup.ts`
- **expectCooperativeFinalization()** (2 connections) — `rea/tests/acceptance/process/processFinalization.test.ts`
- **expectIgnoringFinalization()** (2 connections) — `rea/tests/acceptance/process/processFinalization.test.ts`
- **waitForProcessExit()** (2 connections) — `rea/tests/acceptance/process/processFinalization.test.ts`
- **captureObservations()** (2 connections) — `rea/tests/boundary/process/processCaptureLifecycle.test.ts`
- **execFileAsync** (2 connections) — `rea/tests/boundary/process/processCaptureLifecycle.test.ts`
- **terminateFixtureProcess()** (2 connections) — `rea/tests/boundary/process/processCaptureLifecycle.test.ts`
- **isRecord()** (2 connections) — `rea/tests/support/hostCleanup.ts`
- **CaptureOutcome** (1 connections) — `rea/tests/acceptance/process/processFinalization.test.ts`
- *... and 13 more nodes in this community*

## Relationships

- [vitest](vitest.md) (19 shared connections)
- [ProcessCaptureLifecycle.ts](ProcessCaptureLifecycle.ts.md) (13 shared connections)
- [processScenario.ts](processScenario.ts.md) (10 shared connections)
- [zod](zod.md) (9 shared connections)
- [ref_node_child_process](ref_node_child_process.md) (5 shared connections)
- [ProcessOwnership.ts](ProcessOwnership.ts.md) (4 shared connections)
- [processCapture.ts](processCapture.ts.md) (4 shared connections)
- [createTestTempDirectory](createTestTempDirectory.md) (4 shared connections)
- [createServer.ts](createServer.ts.md) (2 shared connections)
- [processComparison.ts](processComparison.ts.md) (2 shared connections)
- [FilesystemSnapshot.ts](FilesystemSnapshot.ts.md) (2 shared connections)
- [ProviderProcess.ts](ProviderProcess.ts.md) (1 shared connections)

## Source Files

- `rea/src/process/capture/ProcessHarness.ts`
- `rea/tests/acceptance/process/processFinalization.test.ts`
- `rea/tests/boundary/process/processCaptureLifecycle.test.ts`
- `rea/tests/support/hostCleanup.ts`

## Audit Trail

- EXTRACTED: 131 (98%)
- INFERRED: 2 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*