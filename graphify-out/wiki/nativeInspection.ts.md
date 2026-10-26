# nativeInspection.ts

> 172 nodes · cohesion 0.03

## Key Concepts

- **nativeInspection.ts** (59 connections) — `rea/src/domain/native/nativeInspection.ts`
- **nativeCommands.ts** (59 connections) — `rea/tests/fixtures/nativeCommands.ts`
- **MachoImage.fixture.ts** (56 connections) — `rea/src/artifacts/apple/MachoImage.fixture.ts`
- **NativeMacOSProvider** (52 connections) — `rea/src/native/NativeMacOSProvider.ts`
- **NativeFixtureRunner** (52 connections) — `rea/tests/fixtures/nativeCommands.ts`
- **machoImage()** (45 connections) — `rea/src/artifacts/apple/MachoImage.fixture.ts`
- **desktopApplication.test.ts** (44 connections) — `rea/tests/boundary/filesystem/desktopApplication.test.ts`
- **nativeSignatureTargetBinding.test.ts** (41 connections) — `rea/tests/boundary/providers/native/nativeSignatureTargetBinding.test.ts`
- **MachoLoadCommandReader.test.ts** (40 connections) — `rea/src/artifacts/apple/MachoLoadCommandReader.test.ts`
- **nativeInventory.golden.test.ts** (37 connections) — `rea/tests/boundary/providers/native/nativeInventory.golden.test.ts`
- **selectedArtifactSourceLifecycle.test.ts** (35 connections) — `rea/tests/process-global/selectedArtifactSourceLifecycle.test.ts`
- **nativePlistBinarySource.test.ts** (32 connections) — `rea/tests/boundary/providers/native/nativePlistBinarySource.test.ts`
- **plistSourceFormat.test.ts** (32 connections) — `rea/tests/boundary/providers/native/plistSourceFormat.test.ts`
- **nativeMachoTarget()** (32 connections) — `rea/tests/fixtures/nativeCommands.ts`
- **dylibResolutionMcp.test.ts** (31 connections) — `rea/tests/boundary/mcp/dylibResolutionMcp.test.ts`
- **nativeMachoUuidlessInspection.test.ts** (31 connections) — `rea/tests/boundary/providers/native/nativeMachoUuidlessInspection.test.ts`
- **dylibResolutionCli.test.ts** (30 connections) — `rea/tests/boundary/cli/dylibResolutionCli.test.ts`
- **fatImage()** (28 connections) — `rea/src/artifacts/apple/MachoImage.fixture.ts`
- **NativeCommandRunner** (28 connections) — `rea/src/native/CommandRunner.ts`
- **MachOSliceArtifactReader.test.ts** (27 connections) — `rea/src/artifacts/MachOSliceArtifactReader.test.ts`
- **NativeMachoInspection.test.ts** (27 connections) — `rea/src/native/NativeMachoInspection.test.ts`
- **artifactInventoryJvmClass.test.ts** (26 connections) — `rea/tests/acceptance/artifactInventoryJvmClass.test.ts`
- **CPU** (25 connections) — `rea/src/artifacts/apple/MachoImage.fixture.ts`
- **nativeSignatureTargetBindingMcp.test.ts** (25 connections) — `rea/tests/boundary/mcp/nativeSignatureTargetBindingMcp.test.ts`
- **lldbDiscovery.test.ts** (23 connections) — `rea/tests/boundary/providers/native/lldbDiscovery.test.ts`
- *... and 147 more nodes in this community*

## Relationships

- [vitest](vitest.md) (156 shared connections)
- [NativeMacOSProvider.ts](NativeMacOSProvider.ts.md) (44 shared connections)
- [analysisErrorCore.ts](analysisErrorCore.ts.md) (41 shared connections)
- [buffer](buffer.md) (40 shared connections)
- [ok](ok.md) (38 shared connections)
- [zod](zod.md) (38 shared connections)
- [createTestTempDirectory](createTestTempDirectory.md) (36 shared connections)
- [DarwinProcessRunTokenReader.ts](DarwinProcessRunTokenReader.ts.md) (36 shared connections)
- [BinaryTargetResolver.ts](BinaryTargetResolver.ts.md) (27 shared connections)
- [ArtifactReaderFailure](ArtifactReaderFailure.md) (27 shared connections)
- [ArtifactProvider.ts](ArtifactProvider.ts.md) (20 shared connections)
- [result.ts](result.ts.md) (19 shared connections)

## Source Files

- `rea/src/artifacts/MachOSliceArchitecture.test.ts`
- `rea/src/artifacts/MachOSliceArtifactReader.test.ts`
- `rea/src/artifacts/apple/MachoImage.fixture.ts`
- `rea/src/artifacts/apple/MachoLoadCommandReader.test.ts`
- `rea/src/artifacts/inventory/ArtifactGraphConstruction.test.ts`
- `rea/src/composition/desktop.ts`
- `rea/src/domain/apple/dylibResolution.ts`
- `rea/src/domain/native/nativeInspection.ts`
- `rea/src/go/GoMachoImage.alignment.test.ts`
- `rea/src/native/AppleMachoSelection.test.ts`
- `rea/src/native/CommandRunner.ts`
- `rea/src/native/NativeCommandDeadline.test.ts`
- `rea/src/native/NativeMacOSProvider.ts`
- `rea/src/native/NativeMacOSProviderInput.test.ts`
- `rea/src/native/NativeMachoInspection.test.ts`
- `rea/src/native/NativePlistResourceRoot.test.ts`
- `rea/src/rust/RustBinaryImage.machoAlignment.test.ts`
- `rea/tests/acceptance/artifactInventoryJvmClass.test.ts`
- `rea/tests/boundary/cli/dylibResolutionCli.test.ts`
- `rea/tests/boundary/cli/nativeMachoMissingUuidCli.test.ts`

## Audit Trail

- EXTRACTED: 1204 (98%)
- INFERRED: 19 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*