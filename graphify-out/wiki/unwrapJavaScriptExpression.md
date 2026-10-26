# unwrapJavaScriptExpression

> 106 nodes · cohesion 0.05

## Key Concepts

- **unwrapJavaScriptExpression()** (191 connections) — `rea/src/domain/javascript/javascriptAstValues.ts`
- **javascriptStaticAnalysisCalls.ts** (87 connections) — `rea/src/domain/javascript/javascriptStaticAnalysisCalls.ts`
- **javascriptModuleInterop.ts** (48 connections) — `rea/src/domain/javascript/javascriptModuleInterop.ts`
- **semanticStableInitializer()** (42 connections) — `rea/src/domain/javascript/javascriptSemanticState.ts`
- **isUnmodifiedGlobalReference()** (41 connections) — `rea/src/domain/javascript/javascriptSemanticAmbientWrites.ts`
- **javascriptSemanticOpaqueEffects.ts** (35 connections) — `rea/src/domain/javascript/javascriptSemanticOpaqueEffects.ts`
- **createSemanticModuleInterop()** (33 connections) — `rea/src/domain/javascript/javascriptModuleInterop.ts`
- **analyzeParsedJavaScriptStaticSourceSteps()** (27 connections) — `rea/src/domain/javascript/javascriptStaticAnalysis.ts`
- **readExactJavaScriptLiteral()** (22 connections) — `rea/src/domain/javascript/javascriptAstValues.ts`
- **inspectCall()** (22 connections) — `rea/src/domain/javascript/javascriptStaticAnalysisCalls.ts`
- **electronStaticRenderer.ts** (20 connections) — `rea/src/domain/javascript/electronStaticRenderer.ts`
- **javascriptSemanticMapOperations.ts** (19 connections) — `rea/src/domain/javascript/javascriptSemanticMapOperations.ts`
- **javascriptIntrinsicInvocation.ts** (18 connections) — `rea/src/domain/javascript/javascriptIntrinsicInvocation.ts`
- **javascriptStaticPathIntrinsics.ts** (18 connections) — `rea/src/domain/javascript/javascriptStaticPathIntrinsics.ts`
- **resolveElectronBrowserWindowReceiver()** (16 connections) — `rea/src/domain/javascript/electronStaticRenderer.ts`
- **isIntrinsicMapLookup()** (15 connections) — `rea/src/domain/javascript/javascriptSemanticMapOperations.ts`
- **inspectEndpointCall()** (15 connections) — `rea/src/domain/javascript/javascriptStaticAnalysisCalls.ts`
- **semanticRequireCallAt()** (14 connections) — `rea/src/domain/javascript/javascriptSemanticRequireOrigin.ts`
- **javascriptSemanticTypedArrays.ts** (14 connections) — `rea/src/domain/javascript/javascriptSemanticTypedArrays.ts`
- **inspectNode()** (14 connections) — `rea/src/domain/javascript/javascriptStaticAnalysis.ts`
- **childNodes()** (13 connections) — `rea/src/domain/javascript/javascriptSemanticTraversal.ts`
- **semanticFactoryLoaderMemberAt()** (12 connections) — `rea/src/domain/javascript/javascriptSemanticRequireOrigin.ts`
- **addEndpoint()** (12 connections) — `rea/src/domain/javascript/javascriptStaticAnalysisCalls.ts`
- **urlObjectRequestTarget()** (12 connections) — `rea/src/domain/javascript/javascriptStaticAnalysisCalls.ts`
- **electronMemberPath()** (10 connections) — `rea/src/domain/javascript/javascriptElectronMemberWrites.ts`
- *... and 81 more nodes in this community*

## Relationships

- [resolveSemanticBindingState](resolveSemanticBindingState.md) (114 shared connections)
- [javascriptSemanticRequireOrigin.ts](javascriptSemanticRequireOrigin.ts.md) (113 shared connections)
- [javascriptSemanticAnalysis.ts](javascriptSemanticAnalysis.ts.md) (85 shared connections)
- [semanticStaticPropertyKey](semanticStaticPropertyKey.md) (77 shared connections)
- [javascriptStaticAnalysisHelpers.ts](javascriptStaticAnalysisHelpers.ts.md) (64 shared connections)
- [javascriptRouteScan.ts](javascriptRouteScan.ts.md) (46 shared connections)
- [javascriptStaticAnalysisBundler.ts](javascriptStaticAnalysisBundler.ts.md) (23 shared connections)
- [javascriptStaticAnalysis.ts](javascriptStaticAnalysis.ts.md) (22 shared connections)
- [compareUnicodeCodePoints](compareUnicodeCodePoints.md) (22 shared connections)
- [javascriptSemanticMutationInitializers.ts](javascriptSemanticMutationInitializers.ts.md) (17 shared connections)
- [javascriptGraphqlOperations.ts](javascriptGraphqlOperations.ts.md) (10 shared connections)
- [electronWrappedCallPaths.ts](electronWrappedCallPaths.ts.md) (7 shared connections)

## Source Files

- `rea/src/domain/javascript/electronStaticRenderer.ts`
- `rea/src/domain/javascript/javascriptAstValues.ts`
- `rea/src/domain/javascript/javascriptElectronMemberWrites.ts`
- `rea/src/domain/javascript/javascriptIntrinsicInvocation.ts`
- `rea/src/domain/javascript/javascriptModuleInterop.ts`
- `rea/src/domain/javascript/javascriptSemanticAmbientWrites.ts`
- `rea/src/domain/javascript/javascriptSemanticAnalysis.ts`
- `rea/src/domain/javascript/javascriptSemanticDataEffects.ts`
- `rea/src/domain/javascript/javascriptSemanticEvaluationOrder.ts`
- `rea/src/domain/javascript/javascriptSemanticMapOperations.ts`
- `rea/src/domain/javascript/javascriptSemanticOpaqueEffects.ts`
- `rea/src/domain/javascript/javascriptSemanticRequireOrigin.ts`
- `rea/src/domain/javascript/javascriptSemanticState.ts`
- `rea/src/domain/javascript/javascriptSemanticTraversal.ts`
- `rea/src/domain/javascript/javascriptSemanticTypedArrays.ts`
- `rea/src/domain/javascript/javascriptSourceParser.ts`
- `rea/src/domain/javascript/javascriptStaticAnalysis.mapEndpoints.test.ts`
- `rea/src/domain/javascript/javascriptStaticAnalysis.ts`
- `rea/src/domain/javascript/javascriptStaticAnalysisCalls.ts`
- `rea/src/domain/javascript/javascriptStaticAnalysisHelpers.ts`

## Audit Trail

- EXTRACTED: 866 (98%)
- INFERRED: 16 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*