# javascriptSemanticAnalysis.ts

> 279 nodes · cohesion 0.02

## Key Concepts

- **javascriptSemanticAnalysis.ts** (263 connections) — `rea/src/domain/javascript/javascriptSemanticAnalysis.ts`
- **@babel/types** (112 connections) — `rea/package.json`
- **analyzeJavaScriptSemantics()** (94 connections) — `rea/src/domain/javascript/javascriptSemanticAnalysis.ts`
- **javascriptSemanticTraversal.ts** (81 connections) — `rea/src/domain/javascript/javascriptSemanticTraversal.ts`
- **javascriptSourceParser.ts** (80 connections) — `rea/src/domain/javascript/javascriptSourceParser.ts`
- **parseJavaScriptSource()** (77 connections) — `rea/src/domain/javascript/javascriptSourceParser.ts`
- **completeSemanticSteps()** (57 connections) — `rea/src/domain/javascript/javascriptSemanticTraversal.ts`
- **traverseJavaScriptAst()** (49 connections) — `rea/src/domain/javascript/javascriptSemanticTraversal.ts`
- **javascriptSemanticAnalysis.fixture.ts** (41 connections) — `rea/src/domain/javascript/javascriptSemanticAnalysis.fixture.ts`
- **javascriptSemanticExpressionShapes.ts** (35 connections) — `rea/src/domain/javascript/javascriptSemanticExpressionShapes.ts`
- **referenceSourceImportParsing.ts** (32 connections) — `rea/src/domain/referenceSourceImportParsing.ts`
- **indexJavaScriptBindingsWithReceiversSteps()** (30 connections) — `rea/src/domain/javascript/javascriptSemanticAnalysis.ts`
- **referenceSourceRequireBindings.ts** (30 connections) — `rea/src/domain/referenceSourceRequireBindings.ts`
- **collectDefinitionsSteps()** (29 connections) — `rea/src/domain/javascript/javascriptSemanticAnalysis.ts`
- **onlyCallable()** (28 connections) — `rea/src/domain/javascript/javascriptSemanticAnalysis.fixture.ts`
- **javascriptModuleDeclaration.ts** (24 connections) — `rea/src/domain/javascript/javascriptModuleDeclaration.ts`
- **indexJavaScriptElectronIdentitySteps()** (23 connections) — `rea/src/domain/javascript/javascriptSemanticAnalysis.ts`
- **javascriptMemberMutationCoverage.test.ts** (22 connections) — `rea/src/domain/javascript/javascriptMemberMutationCoverage.test.ts`
- **electronStaticReceiverAdmission.test.ts** (21 connections) — `rea/src/domain/javascript/electronStaticReceiverAdmission.test.ts`
- **analyzeParsedJavaScriptSemanticsSteps()** (21 connections) — `rea/src/domain/javascript/javascriptSemanticAnalysis.ts`
- **createSemanticExpressionShapeResolver()** (21 connections) — `rea/src/domain/javascript/javascriptSemanticExpressionShapes.ts`
- **isTypeOnlyExportDeclaration()** (20 connections) — `rea/src/domain/javascript/javascriptModuleDeclaration.ts`
- **analyzeParsedJavaScriptSemantics()** (20 connections) — `rea/src/domain/javascript/javascriptSemanticAnalysis.ts`
- **indexJavaScriptBindingsSteps()** (20 connections) — `rea/src/domain/javascript/javascriptSemanticAnalysis.ts`
- **javascriptStaticAnalysis.mapEndpoints.test.ts** (20 connections) — `rea/src/domain/javascript/javascriptStaticAnalysis.mapEndpoints.test.ts`
- *... and 254 more nodes in this community*

## Relationships

- [resolveSemanticBindingState](resolveSemanticBindingState.md) (101 shared connections)
- [semanticStaticPropertyKey](semanticStaticPropertyKey.md) (100 shared connections)
- [javascriptSemanticRequireOrigin.ts](javascriptSemanticRequireOrigin.ts.md) (87 shared connections)
- [javascriptStaticAnalysis.ts](javascriptStaticAnalysis.ts.md) (86 shared connections)
- [unwrapJavaScriptExpression](unwrapJavaScriptExpression.md) (85 shared connections)
- [vitest](vitest.md) (79 shared connections)
- [compareUnicodeCodePoints](compareUnicodeCodePoints.md) (44 shared connections)
- [javascriptStaticAnalysisHelpers.ts](javascriptStaticAnalysisHelpers.ts.md) (30 shared connections)
- [javascriptStaticAnalysisBundler.ts](javascriptStaticAnalysisBundler.ts.md) (29 shared connections)
- [electronWrappedCallPaths.ts](electronWrappedCallPaths.ts.md) (28 shared connections)
- [javascriptRouteScan.ts](javascriptRouteScan.ts.md) (26 shared connections)
- [WebSourceMapFetcher.ts](WebSourceMapFetcher.ts.md) (20 shared connections)

## Source Files

- `rea/package.json`
- `rea/src/application/javascript/JavaScriptWrappedCallPathCancellation.test.ts`
- `rea/src/domain/javascript/childProcessOptionsRegression.test.ts`
- `rea/src/domain/javascript/electronCallPathBlockPrefixes.test.ts`
- `rea/src/domain/javascript/electronOpaqueBindingIdentity.test.ts`
- `rea/src/domain/javascript/electronStaticReceiverAdmission.test.ts`
- `rea/src/domain/javascript/javascriptElectronMemberWrites.ts`
- `rea/src/domain/javascript/javascriptIntrinsicInvocation.test.ts`
- `rea/src/domain/javascript/javascriptMemberMutationCoverage.test.ts`
- `rea/src/domain/javascript/javascriptModuleDeclaration.ts`
- `rea/src/domain/javascript/javascriptRouteScan.test.ts`
- `rea/src/domain/javascript/javascriptSemanticAmbientWrites.test.ts`
- `rea/src/domain/javascript/javascriptSemanticAnalysis.accessor_invocations.test.ts`
- `rea/src/domain/javascript/javascriptSemanticAnalysis.accessor_writes.test.ts`
- `rea/src/domain/javascript/javascriptSemanticAnalysis.calls.test.ts`
- `rea/src/domain/javascript/javascriptSemanticAnalysis.conditional_write.test.ts`
- `rea/src/domain/javascript/javascriptSemanticAnalysis.dataflow.test.ts`
- `rea/src/domain/javascript/javascriptSemanticAnalysis.empty_keys.test.ts`
- `rea/src/domain/javascript/javascriptSemanticAnalysis.eval_effects.test.ts`
- `rea/src/domain/javascript/javascriptSemanticAnalysis.export_lifetimes.test.ts`

## Audit Trail

- EXTRACTED: 1747 (99%)
- INFERRED: 11 (1%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*