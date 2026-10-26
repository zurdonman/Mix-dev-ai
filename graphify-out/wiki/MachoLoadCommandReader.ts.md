# MachoLoadCommandReader.ts

> 73 nodes · cohesion 0.07

## Key Concepts

- **MachoLoadCommandReader.ts** (64 connections) — `rea/src/artifacts/apple/MachoLoadCommandReader.ts`
- **machoContainer.ts** (39 connections) — `rea/src/domain/apple/machoContainer.ts`
- **ArtifactClassificationProbe.ts** (30 connections) — `rea/src/artifacts/ArtifactClassificationProbe.ts`
- **readFatContainerHeader()** (29 connections) — `rea/src/domain/apple/machoContainer.ts`
- **readMachoHeaderPrefixFacts()** (28 connections) — `rea/src/domain/apple/machoContainer.ts`
- **MachoSliceSelection.ts** (23 connections) — `rea/src/native/metadata/MachoSliceSelection.ts`
- **machoContainer.test.ts** (21 connections) — `rea/src/artifacts/apple/machoContainer.test.ts`
- **MachoFormatIssue** (18 connections) — `rea/src/artifacts/apple/MachoLoadCommandReader.ts`
- **readMachoImage()** (18 connections) — `rea/src/artifacts/apple/MachoLoadCommandReader.ts`
- **classifyFatContainerIdentity()** (17 connections) — `rea/src/domain/apple/machoContainer.ts`
- **validateFatSlice()** (15 connections) — `rea/src/domain/apple/machoContainer.ts`
- **inspectHopperMachOImage()** (14 connections) — `rea/src/hopper/HopperMachOImage.ts`
- **validateFatSliceIdentity()** (13 connections) — `rea/src/domain/apple/machoContainer.ts`
- **readFatSliceDeclarations()** (12 connections) — `rea/src/domain/apple/machoContainer.ts`
- **decodeCommands()** (11 connections) — `rea/src/artifacts/apple/MachoLoadCommandReader.ts`
- **readSlice()** (11 connections) — `rea/src/artifacts/apple/MachoLoadCommandReader.ts`
- **decodeCommand()** (9 connections) — `rea/src/artifacts/apple/MachoLoadCommandReader.ts`
- **hasMachoMagic()** (9 connections) — `rea/src/artifacts/apple/MachoLoadCommandReader.ts`
- **viewOf()** (9 connections) — `rea/src/artifacts/apple/MachoLoadCommandReader.ts`
- **originalOffset()** (9 connections) — `rea/src/hopper/HopperFileOffset.ts`
- **selectNativeImage()** (9 connections) — `rea/src/native/metadata/MachoSliceSelection.ts`
- **readAppleHiddenArm64Slice()** (7 connections) — `rea/src/artifacts/apple/MachoLoadCommandReader.ts`
- **ArtifactClassificationEvidence** (7 connections) — `rea/src/artifacts/ArtifactClassificationProbe.ts`
- **carrierPathDialect()** (7 connections) — `rea/src/artifacts/PyInstallerArtifactReader.ts`
- **decodeDependency()** (6 connections) — `rea/src/artifacts/apple/MachoLoadCommandReader.ts`
- *... and 48 more nodes in this community*

## Relationships

- [ok](ok.md) (39 shared connections)
- [scanCanonical.ts](scanCanonical.ts.md) (20 shared connections)
- [nativeInspection.ts](nativeInspection.ts.md) (14 shared connections)
- [ArtifactReaderFailure](ArtifactReaderFailure.md) (13 shared connections)
- [analysisErrorCore.ts](analysisErrorCore.ts.md) (10 shared connections)
- [AppleMachoFixups.ts](AppleMachoFixups.ts.md) (9 shared connections)
- [PyInstallerArtifactReader.ts](PyInstallerArtifactReader.ts.md) (9 shared connections)
- [BinaryTargetResolver.ts](BinaryTargetResolver.ts.md) (8 shared connections)
- [OwnedFileHandle](OwnedFileHandle.md) (8 shared connections)
- [AnalysisInputError](AnalysisInputError.md) (6 shared connections)
- [buffer](buffer.md) (5 shared connections)
- [ref_node_crypto](ref_node_crypto.md) (5 shared connections)

## Source Files

- `rea/src/artifacts/ArtifactClassificationProbe.ts`
- `rea/src/artifacts/AsarHeader.ts`
- `rea/src/artifacts/PyInstallerArtifactReader.ts`
- `rea/src/artifacts/apple/MachoLoadCommandReader.ts`
- `rea/src/artifacts/apple/machoContainer.test.ts`
- `rea/src/artifacts/inventory/ArtifactGraphConstruction.ts`
- `rea/src/domain/apple/machoContainer.ts`
- `rea/src/domain/apple/machoTargetSelection.ts`
- `rea/src/domain/dosMz.ts`
- `rea/src/hopper/HopperFileOffset.ts`
- `rea/src/hopper/HopperMachOImage.ts`
- `rea/src/native/metadata/MachoSliceSelection.ts`

## Audit Trail

- EXTRACTED: 387 (99%)
- INFERRED: 2 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*