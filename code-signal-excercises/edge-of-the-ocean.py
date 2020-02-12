'''const adjacentElementsProduct = (arr) => {
    let output = arr[0] * arr[1]
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] * arr [i+1] > output) {
            output = arr[i] * arr [i+1]
        }
    }   
    return output
}'''