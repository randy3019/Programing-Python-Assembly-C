package main

import (

	"fmt"

)

func main(){

	// deklarasi variabel:
	fmt.Println("Masukan nilai lebar: ")
	var lebar int8 
	
	
	// saving
    fmt.Scanln(&lebar)
    fmt.Println("Masukan nilai panjang: ")
	var panjang int8 
    fmt.Scanln(&panjang)
    
	
   
    
	// memanggil  Println() function
	
	var luas = lebar * panjang 
    fmt.Println("luas persegi adalah", luas)
}

