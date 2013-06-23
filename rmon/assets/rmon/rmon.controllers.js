define([], function() {
  function DashboardCtrl($scope) {
  };
  DashboardCtrl.$inject = ['$scope'];

  function RMonCtrls($scope) {
    $scope.DashboardCtrl = DashboardCtrl;
  };
  RMonCtrls.$inject = ['$scope'];
  
  return {
    RMonCtrls: RMonCtrls
  };
});