<?php


class SocksMatch
{

    public $array;

    function __construct($array)
    {
        $this->array = $array;
    }

    function getQtyOfPair()
    {
        $length = count($this->array);
        $array = $this->array;
        $qty = 0;
        for ($i = 0; $i < $length; $i++) {
            for ($j = $i+1; $j < $length; $j++) {
                if(($array[$i] == $array[$j]) and ($array[$j] != 'x')) {
                    $array[$i] = $array[$j] = 'x';
                    $qty++;
                }
            }           
        } 
        return $qty;
    }
}


$test_1 = [1, 2, 1, 2, 1, 3, 2]; # resutl 2
$test_2 = [10, 20, 20, 10, 10, 30, 50, 10, 20]; # resutl 3

$result = new SocksMatch($test_2);
echo($result->getQtyOfPair());