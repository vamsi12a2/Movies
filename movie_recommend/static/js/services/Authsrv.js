angular.module("movies").
service("Auth",['$http',function($http){

    this.login = function(username,password){

        return $http({
            url:"./user",
            method:"post",
            data:{username:username,password:password}
        }).then(function(res){
            return res
        })

    }

    this.register = function(first_name,last_name,username,password){
                return $http({
                    url:"./register",
                    method:"post",
                    data:{firstname:first_name,lastname:last_name,username:username,password:password}
                }).then(function(res){
                    return res
                })
        
            }
        

    return this;

}])