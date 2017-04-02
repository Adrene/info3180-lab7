/* global angular */

var app = angular.module("imageApp", []);

app.controller("imgCtrl", function($scope, $http){
    $http.get('/api/thumbnails').then(function(response){
        $scope.images = response.data["thumbnails"];
    });
});