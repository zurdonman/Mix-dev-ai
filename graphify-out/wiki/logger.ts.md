# logger.ts

> 223 nodes · cohesion 0.02

## Key Concepts

- **logger.ts** (100 connections) — `rea/src/logger.ts`
- **parseConfig()** (99 connections) — `rea/src/config/parseConfig.ts`
- **parseConfig.ts** (94 connections) — `rea/src/config/parseConfig.ts`
- **silentLogger** (92 connections) — `rea/src/logger.ts`
- **AnalysisProviderRegistry** (66 connections) — `rea/src/application/binary/AnalysisProviderRegistry.ts`
- **composition/binary.ts** (63 connections) — `rea/src/composition/binary.ts`
- **GhidraProvider** (61 connections) — `rea/src/ghidra/GhidraProvider.ts`
- **directAnalysisCleanup.test.ts** (60 connections) — `rea/tests/composition/directAnalysisCleanup.test.ts`
- **ghidraMcpHarness.ts** (58 connections) — `rea/tests/boundary/mcp/ghidraMcpHarness.ts`
- **ghidraJavaLaunch.test.ts** (56 connections) — `rea/tests/boundary/providers/ghidra/ghidraJavaLaunch.test.ts`
- **ghidraPspExtension.test.ts** (47 connections) — `rea/tests/boundary/filesystem/ghidraPspExtension.test.ts`
- **ghidraReopen.test.ts** (47 connections) — `rea/tests/boundary/mcp/ghidraReopen.test.ts`
- **GhidraMipsProfile.test.ts** (41 connections) — `rea/src/ghidra/GhidraMipsProfile.test.ts`
- **ghidraFailureDiagnostics.test.ts** (41 connections) — `rea/tests/boundary/mcp/ghidraFailureDiagnostics.test.ts`
- **ghidraInventoryMcp.test.ts** (41 connections) — `rea/tests/boundary/mcp/ghidraInventoryMcp.test.ts`
- **directAnalysis.ts** (39 connections) — `rea/src/composition/directAnalysis.ts`
- **ghidraImportSnapshotLifetime.test.ts** (39 connections) — `rea/tests/process-global/ghidraImportSnapshotLifetime.test.ts`
- **composeBinarySession()** (36 connections) — `rea/src/application/binary/BinarySessionComposition.ts`
- **GhidraDolProfile.test.ts** (36 connections) — `rea/src/ghidra/GhidraDolProfile.test.ts`
- **ghidraProfileArtifactOwnership.test.ts** (36 connections) — `rea/tests/boundary/filesystem/ghidraProfileArtifactOwnership.test.ts`
- **ghidraOomRetention.test.ts** (36 connections) — `rea/tests/boundary/providers/ghidra/ghidraOomRetention.test.ts`
- **officialTools.test.ts** (34 connections) — `rea/tests/boundary/mcp/officialTools.test.ts`
- **BinarySessionComposition.ts** (33 connections) — `rea/src/application/binary/BinarySessionComposition.ts`
- **DirectAnalysisStatus.ts** (33 connections) — `rea/src/application/DirectAnalysisStatus.ts`
- **GhidraAnalysisSeeds.test.ts** (32 connections) — `rea/src/ghidra/GhidraAnalysisSeeds.test.ts`
- *... and 198 more nodes in this community*

## Relationships

- [zod](zod.md) (222 shared connections)
- [vitest](vitest.md) (220 shared connections)
- [AnalysisProvider.ts](AnalysisProvider.ts.md) (155 shared connections)
- [analysisErrorCore.ts](analysisErrorCore.ts.md) (96 shared connections)
- [AnalysisCancelledError](AnalysisCancelledError.md) (53 shared connections)
- [BinaryTargetResolver.ts](BinaryTargetResolver.ts.md) (50 shared connections)
- [ok](ok.md) (49 shared connections)
- [projectAnalysisError](projectAnalysisError.md) (43 shared connections)
- [GhidraLauncher.ts](GhidraLauncher.ts.md) (43 shared connections)
- [createTestTempDirectory](createTestTempDirectory.md) (35 shared connections)
- [AnalysisInputError](AnalysisInputError.md) (32 shared connections)
- [GhidraAnalysisProfile.ts](GhidraAnalysisProfile.ts.md) (32 shared connections)

## Source Files

- `rea/src/application/DirectAnalysisDependencies.ts`
- `rea/src/application/DirectAnalysisStatus.ts`
- `rea/src/application/binary/AnalysisProviderRegistry.ts`
- `rea/src/application/binary/BinarySessionComposition.ts`
- `rea/src/application/binary/BundleResourceSession.ts`
- `rea/src/application/binary/SessionProviderRouter.ts`
- `rea/src/cliHostInputs.test.ts`
- `rea/src/composition/binary.ts`
- `rea/src/composition/directAnalysis.ts`
- `rea/src/config/parseConfig.ts`
- `rea/src/config/runtimeAnalysisSettings.ts`
- `rea/src/ghidra/GhidraAnalysisProfile.ts`
- `rea/src/ghidra/GhidraAnalysisSeeds.test.ts`
- `rea/src/ghidra/GhidraClient.ts`
- `rea/src/ghidra/GhidraDoctor.test.ts`
- `rea/src/ghidra/GhidraDolProfile.test.ts`
- `rea/src/ghidra/GhidraInstallation.fixture.ts`
- `rea/src/ghidra/GhidraInstallation.test.ts`
- `rea/src/ghidra/GhidraJavaProbe.ts`
- `rea/src/ghidra/GhidraLanguageOverride.test.ts`

## Audit Trail

- EXTRACTED: 2110 (98%)
- INFERRED: 35 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*