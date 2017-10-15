angular.module("movies").
controller('RegisterCntrl',['$scope','Auth','$location',function($scope,Auth,$location){

    $scope.register =  function(first_name,last_name,username,password,re_password)
    {
        console.log('Register method')
        if(password === re_password){

            Auth.register(first_name,last_name,username,password).then(
                function(res)
                {
                    console.log(res.status)
                    $location.path("/")
                }
            )

        }
       
    }
}])