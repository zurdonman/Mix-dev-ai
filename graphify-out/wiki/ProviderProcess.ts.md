# ProviderProcess.ts

> 292 nodes · cohesion 0.02

## Key Concepts

- **ProviderProcess.ts** (186 connections) — `rea/src/process/ProviderProcess.ts`
- **spawnOwnedProviderProcess()** (131 connections) — `rea/src/process/ProviderProcess.ts`
- **ref_node_stream** (128 connections)
- **cleanupOwnedProcessGroup()** (114 connections) — `rea/src/process/ProcessOwnership.ts`
- **PrivateRuntimeRoot** (105 connections) — `rea/src/process/PrivateRuntimeRoot.ts`
- **PrivateRuntimeRoot.ts** (98 connections) — `rea/src/process/PrivateRuntimeRoot.ts`
- **OwnedCommand.ts** (92 connections) — `rea/src/process/OwnedCommand.ts`
- **ref_node_timers** (90 connections)
- **SourceMapCommand.ts** (69 connections) — `rea/src/javascript/sourceMaps/SourceMapCommand.ts`
- **ref_node_events** (68 connections)
- **serverLifecycleMcp.test.ts** (60 connections) — `rea/tests/boundary/mcp/serverLifecycleMcp.test.ts`
- **nativeProvider.test.ts** (59 connections) — `rea/tests/boundary/providers/native/nativeProvider.test.ts`
- **.create()** (55 connections) — `rea/src/process/PrivateRuntimeRoot.ts`
- **createTestWorkspace()** (50 connections) — `rea/tests/support/workspace/workspaceFixture.ts`
- **removeTestWorkspace()** (50 connections) — `rea/tests/support/workspace/workspaceFixture.ts`
- **recordedCrashProvider.test.ts** (45 connections) — `rea/tests/boundary/binaryDiagnostics/recordedCrashProvider.test.ts`
- **workspaceFixture.ts** (43 connections) — `rea/tests/support/workspace/workspaceFixture.ts`
- **sqliteDatabaseProvider.test.ts** (40 connections) — `rea/tests/boundary/sqlite/sqliteDatabaseProvider.test.ts`
- **pwntoolsCliFinalization.test.ts** (39 connections) — `rea/tests/process-global/pwntoolsCliFinalization.test.ts`
- **pwntoolsStageRetirement.test.ts** (39 connections) — `rea/tests/process-global/pwntoolsStageRetirement.test.ts`
- **sqliteDatabaseDescriptorCleanup.test.ts** (36 connections) — `rea/tests/boundary/sqlite/sqliteDatabaseDescriptorCleanup.test.ts`
- **nativeVerifierPreflightOwnership.test.ts** (31 connections) — `rea/tests/boundary/process/nativeVerifierPreflightOwnership.test.ts`
- **evmoleInterfaceProvider.test.ts** (30 connections) — `rea/tests/boundary/evm/evmoleInterfaceProvider.test.ts`
- **ownedCommand.test.ts** (29 connections) — `rea/tests/boundary/process/ownedCommand.test.ts`
- **providerProcess.test.ts** (29 connections) — `rea/tests/boundary/process/providerProcess.test.ts`
- *... and 267 more nodes in this community*

## Relationships

- [vitest](vitest.md) (160 shared connections)
- [analysisErrorCore.ts](analysisErrorCore.ts.md) (128 shared connections)
- [ProcessOwnership.ts](ProcessOwnership.ts.md) (119 shared connections)
- [PwntoolsDecoder.ts](PwntoolsDecoder.ts.md) (67 shared connections)
- [JavaScriptAnalysisWorker.ts](JavaScriptAnalysisWorker.ts.md) (63 shared connections)
- [zod](zod.md) (59 shared connections)
- [HopperClient.ts](HopperClient.ts.md) (57 shared connections)
- [analysisErrorProjection.ts](analysisErrorProjection.ts.md) (55 shared connections)
- [ExecutionOptions](ExecutionOptions.md) (54 shared connections)
- [ProviderProcessSupervisor](ProviderProcessSupervisor.md) (49 shared connections)
- [AnalysisCancelledError](AnalysisCancelledError.md) (47 shared connections)
- [buffer](buffer.md) (42 shared connections)

## Source Files

- `rea/src/adb/AdbProvider.ts`
- `rea/src/android/JadxMcpTransport.ts`
- `rea/src/android/JadxProvider.ts`
- `rea/src/android/JadxSession.ts`
- `rea/src/application/UpdateCommandProgress.test.ts`
- `rea/src/application/UpdateCommandProgress.ts`
- `rea/src/application/binaryDiagnostics/RecordedCrashService.test.ts`
- `rea/src/application/sqlite/SqliteDatabasePort.ts`
- `rea/src/application/sqlite/SqliteDatabaseService.ts`
- `rea/src/browser/ElectronCaptureCleanup.boundary.test.ts`
- `rea/src/browser/WebBundleAnalysisWorker.test.ts`
- `rea/src/browser/WebBundleAnalysisWorkerReadCompletion.test.ts`
- `rea/src/composition/sqlite.ts`
- `rea/src/domain/native/recordedCrash.test.ts`
- `rea/src/evm/EvmoleInterfaceProvider.ts`
- `rea/src/firmware/FirmwareCommand.test.ts`
- `rea/src/javascript/sourceMaps/SourceMapCommand.test.ts`
- `rea/src/javascript/sourceMaps/SourceMapCommand.ts`
- `rea/src/javascript/sourceMaps/SourceMapDecoder.test.ts`
- `rea/src/javascript/sourceMaps/SourceMapDecoder.ts`

## Audit Trail

- EXTRACTED: 2514 (99%)
- INFERRED: 26 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*