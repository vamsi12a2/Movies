angular.module("movies").
controller('UserCntrl',['$scope','Auth','$location','$http',function($scope,Auth,$location,$http){
    var page = Math.floor((Math.random() * 10) + 1);
    $scope.$watch('viewContentLoaded', function(){
    var apikey = "abbd4440b5238f02bea5283369797d70"
    $http({
        method:"GET",
        url:"https://api.themoviedb.org/3/discover/movie?page="+page+"&sort_by=popularity.desc&api_key="+apikey
    }).then(function(res){
        $scope.data = res.data
    },function(res){
        console.log(res)
    })
    
 })

}])


