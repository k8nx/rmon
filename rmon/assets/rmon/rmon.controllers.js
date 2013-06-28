define([], function() {
  function DashboardCtrl($scope, $http) {
    $scope.clusters = [];

    $http.get('/v1/clusters/').success(function(json) {
      $scope.clusters = json;
    });
  };
  DashboardCtrl.$inject = ['$scope', '$http'];

  function RMonCtrls($scope) {
    $scope.DashboardCtrl = DashboardCtrl;
  };
  RMonCtrls.$inject = ['$scope'];

  return {
    RMonCtrls: RMonCtrls
  };
});
