# ArtifactProvider.ts

> 161 nodes · cohesion 0.02

## Key Concepts

- **ArtifactProvider.ts** (119 connections) — `rea/src/artifacts/ArtifactProvider.ts`
- **artifactGraph.ts** (115 connections) — `rea/src/domain/artifactGraph.ts`
- **artifactInspection.ts** (99 connections) — `rea/src/domain/artifactInspection.ts`
- **ArtifactProvider** (46 connections) — `rea/src/artifacts/ArtifactProvider.ts`
- **artifactToolContracts.ts** (45 connections) — `rea/src/contracts/artifactToolContracts.ts`
- **artifactZipIntegrity.test.ts** (34 connections) — `rea/tests/boundary/filesystem/artifactZipIntegrity.test.ts`
- **dylibFileLifetime.test.ts** (27 connections) — `rea/tests/process-global/dylibFileLifetime.test.ts`
- **cliJsonInput.test.ts** (26 connections) — `rea/tests/boundary/filesystem/cliJsonInput.test.ts`
- **keyedArchiveSelection.test.ts** (26 connections) — `rea/tests/boundary/filesystem/keyedArchiveSelection.test.ts`
- **wakaruIntegration.test.ts** (26 connections) — `rea/tests/boundary/javascript-recovery/wakaruIntegration.test.ts`
- **artifactProvider.archiveSafety.test.ts** (26 connections) — `rea/tests/boundary/providers/native/artifactProvider.archiveSafety.test.ts`
- **KeyedArchiveRawRefusal.test.ts** (24 connections) — `rea/src/artifacts/apple/KeyedArchiveRawRefusal.test.ts`
- **inspectBundleKeyedArchive()** (24 connections) — `rea/src/artifacts/apple/KeyedArchiveReader.ts`
- **artifactProvider.archiveInventory.test.ts** (24 connections) — `rea/tests/boundary/providers/native/artifactProvider.archiveInventory.test.ts`
- **KeyedArchiveReadFailure.test.ts** (23 connections) — `rea/src/artifacts/apple/KeyedArchiveReadFailure.test.ts`
- **artifactProvider.extractionFormat.test.ts** (23 connections) — `rea/tests/boundary/providers/native/artifactProvider.extractionFormat.test.ts`
- **artifactIntegrity.ts** (20 connections) — `rea/src/domain/artifactIntegrity.ts`
- **machoArmSlices.ts** (20 connections) — `rea/tests/fixtures/machoArmSlices.ts`
- **KeyedArchiveHostDenial.test.ts** (19 connections) — `rea/src/artifacts/apple/KeyedArchiveHostDenial.test.ts`
- **artifactProvider.cleanupRetry.test.ts** (19 connections) — `rea/tests/boundary/providers/native/artifactProvider.cleanupRetry.test.ts`
- **artifactProvider.universalExtraction.test.ts** (19 connections) — `rea/tests/boundary/providers/native/artifactProvider.universalExtraction.test.ts`
- **safeOutputTreeCloseFailures.test.ts** (18 connections) — `rea/tests/boundary/filesystem/safeOutputTreeCloseFailures.test.ts`
- **artifactArmSlicesMcp.test.ts** (18 connections) — `rea/tests/boundary/mcp/artifactArmSlicesMcp.test.ts`
- **asarListingAdmissionMcp.test.ts** (17 connections) — `rea/tests/boundary/mcp/asarListingAdmissionMcp.test.ts`
- **openBinaryFifo.test.ts** (17 connections) — `rea/tests/boundary/mcp/openBinaryFifo.test.ts`
- *... and 136 more nodes in this community*

## Relationships

- [vitest](vitest.md) (196 shared connections)
- [zod](zod.md) (70 shared connections)
- [ArtifactReaderFailure](ArtifactReaderFailure.md) (58 shared connections)
- [AnalysisProvider.ts](AnalysisProvider.ts.md) (43 shared connections)
- [ref_node_crypto](ref_node_crypto.md) (31 shared connections)
- [createTestTempDirectory](createTestTempDirectory.md) (29 shared connections)
- [buffer](buffer.md) (25 shared connections)
- [artifactInventoryEvidence.ts](artifactInventoryEvidence.ts.md) (24 shared connections)
- [AnalysisInputError](AnalysisInputError.md) (21 shared connections)
- [BinaryTargetResolver.ts](BinaryTargetResolver.ts.md) (20 shared connections)
- [nativeInspection.ts](nativeInspection.ts.md) (20 shared connections)
- [analysisErrorCore.ts](analysisErrorCore.ts.md) (18 shared connections)

## Source Files

- `rea/src/artifacts/ArtifactProvider.ts`
- `rea/src/artifacts/ArtifactProviderMetadata.ts`
- `rea/src/artifacts/apple/KeyedArchiveHostDenial.test.ts`
- `rea/src/artifacts/apple/KeyedArchiveRawRefusal.test.ts`
- `rea/src/artifacts/apple/KeyedArchiveReadFailure.test.ts`
- `rea/src/artifacts/apple/KeyedArchiveReader.ts`
- `rea/src/contracts/artifactToolContracts.ts`
- `rea/src/domain/apple/keyedArchive.ts`
- `rea/src/domain/artifactGraph.ts`
- `rea/src/domain/artifactInspection.ts`
- `rea/src/domain/artifactIntegrity.ts`
- `rea/src/domain/artifactIntegrityPolicy.ts`
- `rea/src/domain/javascript/javascriptArtifactFiles.ts`
- `rea/tests/boundary/cli/artifactArmSlicesCli.test.ts`
- `rea/tests/boundary/filesystem/artifactZipIntegrity.test.ts`
- `rea/tests/boundary/filesystem/cliJsonInput.test.ts`
- `rea/tests/boundary/filesystem/keyedArchiveSelection.test.ts`
- `rea/tests/boundary/filesystem/safeOutputTreeCloseFailures.test.ts`
- `rea/tests/boundary/javascript-recovery/wakaruFileOwnership.test.ts`
- `rea/tests/boundary/javascript-recovery/wakaruIntegration.test.ts`

## Audit Trail

- EXTRACTED: 1057 (100%)
- INFERRED: 3 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*