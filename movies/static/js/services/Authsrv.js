angular.module("movies").
service("Auth",['$http',function($http){
    var data ={}
    this.login = function(username,password){
        return $http({
            url:"./user",
            method:"post",
            data:{username:username,password:password}
        }).then(function(res){
                data = res.data
                return res
        })

       
    }

    this.getData =function(){
        return data
    }

    this.register = function(first_name,last_name,username,password){
            console.log('register service')
                return $http({
                    url:"./register",
                    method:"post",
                    data:{firstname:first_name,lastname:last_name,username:username,password:password}
                }).then(function(res){
                    return res
                })
        
            }
        
    this.logout = function(){

        return $http({
            url:'./logout',
            method:'get'
        }).then(function(res){
            return res
        })
    }
    return this;

}])