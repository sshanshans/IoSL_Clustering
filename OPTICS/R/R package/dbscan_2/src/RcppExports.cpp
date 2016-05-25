// This file was generated by Rcpp::compileAttributes
// Generator token: 10BE3573-1514-4C36-9D1C-5A225CD40393

#include <Rcpp.h>

using namespace Rcpp;

// gradient_clustering
List gradient_clustering(IntegerVector co, NumericVector reachdist, int minPts, float t);
RcppExport SEXP dbscan_gradient_clustering(SEXP coSEXP, SEXP reachdistSEXP, SEXP minPtsSEXP, SEXP tSEXP) {
BEGIN_RCPP
    Rcpp::RObject __result;
    Rcpp::RNGScope __rngScope;
    Rcpp::traits::input_parameter< IntegerVector >::type co(coSEXP);
    Rcpp::traits::input_parameter< NumericVector >::type reachdist(reachdistSEXP);
    Rcpp::traits::input_parameter< int >::type minPts(minPtsSEXP);
    Rcpp::traits::input_parameter< float >::type t(tSEXP);
    __result = Rcpp::wrap(gradient_clustering(co, reachdist, minPts, t));
    return __result;
END_RCPP
}
// dbscan_int
IntegerVector dbscan_int(NumericMatrix data, double eps, int minPts, NumericVector weights, int borderPoints, int type, int bucketSize, int splitRule, double approx, List frNN);
RcppExport SEXP dbscan_dbscan_int(SEXP dataSEXP, SEXP epsSEXP, SEXP minPtsSEXP, SEXP weightsSEXP, SEXP borderPointsSEXP, SEXP typeSEXP, SEXP bucketSizeSEXP, SEXP splitRuleSEXP, SEXP approxSEXP, SEXP frNNSEXP) {
BEGIN_RCPP
    Rcpp::RObject __result;
    Rcpp::RNGScope __rngScope;
    Rcpp::traits::input_parameter< NumericMatrix >::type data(dataSEXP);
    Rcpp::traits::input_parameter< double >::type eps(epsSEXP);
    Rcpp::traits::input_parameter< int >::type minPts(minPtsSEXP);
    Rcpp::traits::input_parameter< NumericVector >::type weights(weightsSEXP);
    Rcpp::traits::input_parameter< int >::type borderPoints(borderPointsSEXP);
    Rcpp::traits::input_parameter< int >::type type(typeSEXP);
    Rcpp::traits::input_parameter< int >::type bucketSize(bucketSizeSEXP);
    Rcpp::traits::input_parameter< int >::type splitRule(splitRuleSEXP);
    Rcpp::traits::input_parameter< double >::type approx(approxSEXP);
    Rcpp::traits::input_parameter< List >::type frNN(frNNSEXP);
    __result = Rcpp::wrap(dbscan_int(data, eps, minPts, weights, borderPoints, type, bucketSize, splitRule, approx, frNN));
    return __result;
END_RCPP
}
// frNN_int
List frNN_int(NumericMatrix data, double eps, int type, int bucketSize, int splitRule, double approx);
RcppExport SEXP dbscan_frNN_int(SEXP dataSEXP, SEXP epsSEXP, SEXP typeSEXP, SEXP bucketSizeSEXP, SEXP splitRuleSEXP, SEXP approxSEXP) {
BEGIN_RCPP
    Rcpp::RObject __result;
    Rcpp::RNGScope __rngScope;
    Rcpp::traits::input_parameter< NumericMatrix >::type data(dataSEXP);
    Rcpp::traits::input_parameter< double >::type eps(epsSEXP);
    Rcpp::traits::input_parameter< int >::type type(typeSEXP);
    Rcpp::traits::input_parameter< int >::type bucketSize(bucketSizeSEXP);
    Rcpp::traits::input_parameter< int >::type splitRule(splitRuleSEXP);
    Rcpp::traits::input_parameter< double >::type approx(approxSEXP);
    __result = Rcpp::wrap(frNN_int(data, eps, type, bucketSize, splitRule, approx));
    return __result;
END_RCPP
}
// kNN_int
List kNN_int(NumericMatrix data, int k, int type, int bucketSize, int splitRule, double approx);
RcppExport SEXP dbscan_kNN_int(SEXP dataSEXP, SEXP kSEXP, SEXP typeSEXP, SEXP bucketSizeSEXP, SEXP splitRuleSEXP, SEXP approxSEXP) {
BEGIN_RCPP
    Rcpp::RObject __result;
    Rcpp::RNGScope __rngScope;
    Rcpp::traits::input_parameter< NumericMatrix >::type data(dataSEXP);
    Rcpp::traits::input_parameter< int >::type k(kSEXP);
    Rcpp::traits::input_parameter< int >::type type(typeSEXP);
    Rcpp::traits::input_parameter< int >::type bucketSize(bucketSizeSEXP);
    Rcpp::traits::input_parameter< int >::type splitRule(splitRuleSEXP);
    Rcpp::traits::input_parameter< double >::type approx(approxSEXP);
    __result = Rcpp::wrap(kNN_int(data, k, type, bucketSize, splitRule, approx));
    return __result;
END_RCPP
}
// optics_int
List optics_int(NumericMatrix data, double eps, int minPts, int type, int bucketSize, int splitRule, double approx, List frNN);
RcppExport SEXP dbscan_optics_int(SEXP dataSEXP, SEXP epsSEXP, SEXP minPtsSEXP, SEXP typeSEXP, SEXP bucketSizeSEXP, SEXP splitRuleSEXP, SEXP approxSEXP, SEXP frNNSEXP) {
BEGIN_RCPP
    Rcpp::RObject __result;
    Rcpp::RNGScope __rngScope;
    Rcpp::traits::input_parameter< NumericMatrix >::type data(dataSEXP);
    Rcpp::traits::input_parameter< double >::type eps(epsSEXP);
    Rcpp::traits::input_parameter< int >::type minPts(minPtsSEXP);
    Rcpp::traits::input_parameter< int >::type type(typeSEXP);
    Rcpp::traits::input_parameter< int >::type bucketSize(bucketSizeSEXP);
    Rcpp::traits::input_parameter< int >::type splitRule(splitRuleSEXP);
    Rcpp::traits::input_parameter< double >::type approx(approxSEXP);
    Rcpp::traits::input_parameter< List >::type frNN(frNNSEXP);
    __result = Rcpp::wrap(optics_int(data, eps, minPts, type, bucketSize, splitRule, approx, frNN));
    return __result;
END_RCPP
}
