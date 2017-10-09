angular.module("movies").
controller('UserCntrl',['$scope','Auth','$location',function($scope,Auth,$location){
    $scope.data = Auth.getData()
}])