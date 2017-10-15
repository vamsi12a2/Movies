angular.module("movies").
service("User",['$http',function($http){

    var apikey = "abbd4440b5238f02bea5283369797d70";
    
    this.get_page = function(){
    var page = Math.floor((Math.random() * 10) + 1);
      return $http({
            method:"GET",
            url:"https://api.themoviedb.org/3/discover/movie?page="+page+"&sort_by=popularity.desc&api_key="+apikey
        }).then(function(res){
            console.log(res.data)
            return res
        })
       }
       

}])