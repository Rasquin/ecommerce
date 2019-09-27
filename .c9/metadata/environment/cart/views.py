{"filter":false,"title":"views.py","tooltip":"/cart/views.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":22,"column":25},"end":{"row":22,"column":25},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"62d73381039faf5a4a233fa0830b00b3fc5c3036","undoManager":{"mark":54,"position":54,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":33,"column":41},"action":"insert","lines":["from django.shortcuts import render, redirect, reverse","","# Create your views here.","def view_cart(request):","    \"\"\"A View that renders the cart contents page\"\"\"","    return render(request, \"cart.html\")","","","def add_to_cart(request, id):","    \"\"\"Add a quantity of the specified product to the cart\"\"\"","    quantity = int(request.POST.get('quantity'))","","    cart = request.session.get('cart', {})","    cart[id] = cart.get(id, quantity)","","    request.session['cart'] = cart","    return redirect(reverse('index'))","","","def adjust_cart(request, id):","    \"\"\"","    Adjust the quantity of the specified product to the specified","    amount","    \"\"\"","    quantity = int(request.POST.get('quantity'))","    cart = request.session.get('cart', {})","","    if quantity > 0:","        cart[id] = quantity","    else:","        cart.pop(id)","    ","    request.session['cart'] = cart","    return redirect(reverse('view_cart'))"]}],[{"start":{"row":16,"column":37},"end":{"row":16,"column":38},"action":"insert","lines":[" "],"id":3},{"start":{"row":16,"column":38},"end":{"row":16,"column":39},"action":"insert","lines":["#"]},{"start":{"row":16,"column":39},"end":{"row":16,"column":40},"action":"insert","lines":["I"]}],[{"start":{"row":16,"column":40},"end":{"row":16,"column":41},"action":"insert","lines":[" "],"id":4},{"start":{"row":16,"column":41},"end":{"row":16,"column":42},"action":"insert","lines":["w"]},{"start":{"row":16,"column":42},"end":{"row":16,"column":43},"action":"insert","lines":["o"]},{"start":{"row":16,"column":43},"end":{"row":16,"column":44},"action":"insert","lines":["u"]},{"start":{"row":16,"column":44},"end":{"row":16,"column":45},"action":"insert","lines":["l"]},{"start":{"row":16,"column":45},"end":{"row":16,"column":46},"action":"insert","lines":["d"]}],[{"start":{"row":16,"column":46},"end":{"row":16,"column":47},"action":"insert","lines":[" "],"id":5},{"start":{"row":16,"column":47},"end":{"row":16,"column":48},"action":"insert","lines":["h"]},{"start":{"row":16,"column":48},"end":{"row":16,"column":49},"action":"insert","lines":["a"]},{"start":{"row":16,"column":49},"end":{"row":16,"column":50},"action":"insert","lines":["v"]},{"start":{"row":16,"column":50},"end":{"row":16,"column":51},"action":"insert","lines":["e"]}],[{"start":{"row":16,"column":51},"end":{"row":16,"column":52},"action":"insert","lines":[" "],"id":6},{"start":{"row":16,"column":52},"end":{"row":16,"column":53},"action":"insert","lines":["r"]},{"start":{"row":16,"column":53},"end":{"row":16,"column":54},"action":"insert","lines":["e"]},{"start":{"row":16,"column":54},"end":{"row":16,"column":55},"action":"insert","lines":["d"]},{"start":{"row":16,"column":55},"end":{"row":16,"column":56},"action":"insert","lines":["i"]},{"start":{"row":16,"column":56},"end":{"row":16,"column":57},"action":"insert","lines":["r"]},{"start":{"row":16,"column":57},"end":{"row":16,"column":58},"action":"insert","lines":["e"]},{"start":{"row":16,"column":58},"end":{"row":16,"column":59},"action":"insert","lines":["c"]},{"start":{"row":16,"column":59},"end":{"row":16,"column":60},"action":"insert","lines":["t"]}],[{"start":{"row":16,"column":60},"end":{"row":16,"column":61},"action":"insert","lines":[" "],"id":7},{"start":{"row":16,"column":61},"end":{"row":16,"column":62},"action":"insert","lines":["t"]},{"start":{"row":16,"column":62},"end":{"row":16,"column":63},"action":"insert","lines":["o"]}],[{"start":{"row":16,"column":63},"end":{"row":16,"column":64},"action":"insert","lines":[" "],"id":8},{"start":{"row":16,"column":64},"end":{"row":16,"column":65},"action":"insert","lines":["p"]},{"start":{"row":16,"column":65},"end":{"row":16,"column":66},"action":"insert","lines":["r"]},{"start":{"row":16,"column":66},"end":{"row":16,"column":67},"action":"insert","lines":["o"]},{"start":{"row":16,"column":67},"end":{"row":16,"column":68},"action":"insert","lines":["d"]},{"start":{"row":16,"column":68},"end":{"row":16,"column":69},"action":"insert","lines":["u"]},{"start":{"row":16,"column":69},"end":{"row":16,"column":70},"action":"insert","lines":["c"]},{"start":{"row":16,"column":70},"end":{"row":16,"column":71},"action":"insert","lines":["t"]}],[{"start":{"row":16,"column":70},"end":{"row":16,"column":71},"action":"remove","lines":["t"],"id":9},{"start":{"row":16,"column":69},"end":{"row":16,"column":70},"action":"remove","lines":["c"]},{"start":{"row":16,"column":68},"end":{"row":16,"column":69},"action":"remove","lines":["u"]},{"start":{"row":16,"column":67},"end":{"row":16,"column":68},"action":"remove","lines":["d"]},{"start":{"row":16,"column":66},"end":{"row":16,"column":67},"action":"remove","lines":["o"]},{"start":{"row":16,"column":65},"end":{"row":16,"column":66},"action":"remove","lines":["r"]},{"start":{"row":16,"column":64},"end":{"row":16,"column":65},"action":"remove","lines":["p"]},{"start":{"row":16,"column":63},"end":{"row":16,"column":64},"action":"remove","lines":[" "]},{"start":{"row":16,"column":62},"end":{"row":16,"column":63},"action":"remove","lines":["o"]},{"start":{"row":16,"column":61},"end":{"row":16,"column":62},"action":"remove","lines":["t"]},{"start":{"row":16,"column":60},"end":{"row":16,"column":61},"action":"remove","lines":[" "]},{"start":{"row":16,"column":59},"end":{"row":16,"column":60},"action":"remove","lines":["t"]},{"start":{"row":16,"column":58},"end":{"row":16,"column":59},"action":"remove","lines":["c"]},{"start":{"row":16,"column":57},"end":{"row":16,"column":58},"action":"remove","lines":["e"]},{"start":{"row":16,"column":56},"end":{"row":16,"column":57},"action":"remove","lines":["r"]},{"start":{"row":16,"column":55},"end":{"row":16,"column":56},"action":"remove","lines":["i"]},{"start":{"row":16,"column":54},"end":{"row":16,"column":55},"action":"remove","lines":["d"]},{"start":{"row":16,"column":53},"end":{"row":16,"column":54},"action":"remove","lines":["e"]},{"start":{"row":16,"column":52},"end":{"row":16,"column":53},"action":"remove","lines":["r"]},{"start":{"row":16,"column":51},"end":{"row":16,"column":52},"action":"remove","lines":[" "]},{"start":{"row":16,"column":50},"end":{"row":16,"column":51},"action":"remove","lines":["e"]},{"start":{"row":16,"column":49},"end":{"row":16,"column":50},"action":"remove","lines":["v"]},{"start":{"row":16,"column":48},"end":{"row":16,"column":49},"action":"remove","lines":["a"]},{"start":{"row":16,"column":47},"end":{"row":16,"column":48},"action":"remove","lines":["h"]}],[{"start":{"row":16,"column":46},"end":{"row":16,"column":47},"action":"remove","lines":[" "],"id":10},{"start":{"row":16,"column":45},"end":{"row":16,"column":46},"action":"remove","lines":["d"]},{"start":{"row":16,"column":44},"end":{"row":16,"column":45},"action":"remove","lines":["l"]},{"start":{"row":16,"column":43},"end":{"row":16,"column":44},"action":"remove","lines":["u"]},{"start":{"row":16,"column":42},"end":{"row":16,"column":43},"action":"remove","lines":["o"]},{"start":{"row":16,"column":41},"end":{"row":16,"column":42},"action":"remove","lines":["w"]}],[{"start":{"row":16,"column":40},"end":{"row":16,"column":41},"action":"remove","lines":[" "],"id":11},{"start":{"row":16,"column":39},"end":{"row":16,"column":40},"action":"remove","lines":["I"]},{"start":{"row":16,"column":38},"end":{"row":16,"column":39},"action":"remove","lines":["#"]},{"start":{"row":16,"column":37},"end":{"row":16,"column":38},"action":"remove","lines":[" "]}],[{"start":{"row":16,"column":37},"end":{"row":16,"column":38},"action":"insert","lines":["#"],"id":12}],[{"start":{"row":16,"column":38},"end":{"row":16,"column":39},"action":"insert","lines":[" "],"id":13},{"start":{"row":16,"column":39},"end":{"row":16,"column":40},"action":"insert","lines":["i"]},{"start":{"row":16,"column":40},"end":{"row":16,"column":41},"action":"insert","lines":["n"]},{"start":{"row":16,"column":41},"end":{"row":16,"column":42},"action":"insert","lines":["d"]},{"start":{"row":16,"column":42},"end":{"row":16,"column":43},"action":"insert","lines":["e"]},{"start":{"row":16,"column":43},"end":{"row":16,"column":44},"action":"insert","lines":["x"]}],[{"start":{"row":16,"column":44},"end":{"row":16,"column":45},"action":"insert","lines":[" "],"id":14},{"start":{"row":16,"column":45},"end":{"row":16,"column":46},"action":"insert","lines":["a"]},{"start":{"row":16,"column":46},"end":{"row":16,"column":47},"action":"insert","lines":["n"]},{"start":{"row":16,"column":47},"end":{"row":16,"column":48},"action":"insert","lines":["d"]}],[{"start":{"row":16,"column":48},"end":{"row":16,"column":49},"action":"insert","lines":[" "],"id":15}],[{"start":{"row":16,"column":48},"end":{"row":16,"column":49},"action":"remove","lines":[" "],"id":16},{"start":{"row":16,"column":47},"end":{"row":16,"column":48},"action":"remove","lines":["d"]},{"start":{"row":16,"column":46},"end":{"row":16,"column":47},"action":"remove","lines":["n"]},{"start":{"row":16,"column":45},"end":{"row":16,"column":46},"action":"remove","lines":["a"]},{"start":{"row":16,"column":44},"end":{"row":16,"column":45},"action":"remove","lines":[" "]},{"start":{"row":16,"column":43},"end":{"row":16,"column":44},"action":"remove","lines":["x"]},{"start":{"row":16,"column":42},"end":{"row":16,"column":43},"action":"remove","lines":["e"]},{"start":{"row":16,"column":41},"end":{"row":16,"column":42},"action":"remove","lines":["d"]},{"start":{"row":16,"column":40},"end":{"row":16,"column":41},"action":"remove","lines":["n"]},{"start":{"row":16,"column":39},"end":{"row":16,"column":40},"action":"remove","lines":["i"]}],[{"start":{"row":16,"column":39},"end":{"row":16,"column":40},"action":"insert","lines":["t"],"id":17},{"start":{"row":16,"column":40},"end":{"row":16,"column":41},"action":"insert","lines":["h"]},{"start":{"row":16,"column":41},"end":{"row":16,"column":42},"action":"insert","lines":["e"]}],[{"start":{"row":16,"column":42},"end":{"row":16,"column":43},"action":"insert","lines":[" "],"id":18},{"start":{"row":16,"column":43},"end":{"row":16,"column":44},"action":"insert","lines":["t"]},{"start":{"row":16,"column":44},"end":{"row":16,"column":45},"action":"insert","lines":["e"]},{"start":{"row":16,"column":45},"end":{"row":16,"column":46},"action":"insert","lines":["m"]},{"start":{"row":16,"column":46},"end":{"row":16,"column":47},"action":"insert","lines":["p"]},{"start":{"row":16,"column":47},"end":{"row":16,"column":48},"action":"insert","lines":["l"]},{"start":{"row":16,"column":48},"end":{"row":16,"column":49},"action":"insert","lines":["a"]},{"start":{"row":16,"column":49},"end":{"row":16,"column":50},"action":"insert","lines":["t"]},{"start":{"row":16,"column":50},"end":{"row":16,"column":51},"action":"insert","lines":["e"]}],[{"start":{"row":16,"column":51},"end":{"row":16,"column":52},"action":"insert","lines":[" "],"id":19},{"start":{"row":16,"column":52},"end":{"row":16,"column":53},"action":"insert","lines":["c"]},{"start":{"row":16,"column":53},"end":{"row":16,"column":54},"action":"insert","lines":["a"]},{"start":{"row":16,"column":54},"end":{"row":16,"column":55},"action":"insert","lines":["l"]},{"start":{"row":16,"column":55},"end":{"row":16,"column":56},"action":"insert","lines":["l"]},{"start":{"row":16,"column":56},"end":{"row":16,"column":57},"action":"insert","lines":["e"]},{"start":{"row":16,"column":57},"end":{"row":16,"column":58},"action":"insert","lines":["d"]}],[{"start":{"row":16,"column":58},"end":{"row":16,"column":59},"action":"insert","lines":[" "],"id":20},{"start":{"row":16,"column":59},"end":{"row":16,"column":60},"action":"insert","lines":["i"]},{"start":{"row":16,"column":60},"end":{"row":16,"column":61},"action":"insert","lines":["n"]},{"start":{"row":16,"column":61},"end":{"row":16,"column":62},"action":"insert","lines":["d"]}],[{"start":{"row":16,"column":61},"end":{"row":16,"column":62},"action":"remove","lines":["d"],"id":21},{"start":{"row":16,"column":60},"end":{"row":16,"column":61},"action":"remove","lines":["n"]},{"start":{"row":16,"column":59},"end":{"row":16,"column":60},"action":"remove","lines":["i"]},{"start":{"row":16,"column":58},"end":{"row":16,"column":59},"action":"remove","lines":[" "]},{"start":{"row":16,"column":57},"end":{"row":16,"column":58},"action":"remove","lines":["d"]},{"start":{"row":16,"column":56},"end":{"row":16,"column":57},"action":"remove","lines":["e"]},{"start":{"row":16,"column":55},"end":{"row":16,"column":56},"action":"remove","lines":["l"]},{"start":{"row":16,"column":54},"end":{"row":16,"column":55},"action":"remove","lines":["l"]},{"start":{"row":16,"column":53},"end":{"row":16,"column":54},"action":"remove","lines":["a"]},{"start":{"row":16,"column":52},"end":{"row":16,"column":53},"action":"remove","lines":["c"]},{"start":{"row":16,"column":51},"end":{"row":16,"column":52},"action":"remove","lines":[" "]},{"start":{"row":16,"column":50},"end":{"row":16,"column":51},"action":"remove","lines":["e"]},{"start":{"row":16,"column":49},"end":{"row":16,"column":50},"action":"remove","lines":["t"]},{"start":{"row":16,"column":48},"end":{"row":16,"column":49},"action":"remove","lines":["a"]},{"start":{"row":16,"column":47},"end":{"row":16,"column":48},"action":"remove","lines":["l"]},{"start":{"row":16,"column":46},"end":{"row":16,"column":47},"action":"remove","lines":["p"]},{"start":{"row":16,"column":45},"end":{"row":16,"column":46},"action":"remove","lines":["m"]}],[{"start":{"row":16,"column":44},"end":{"row":16,"column":45},"action":"remove","lines":["e"],"id":22},{"start":{"row":16,"column":43},"end":{"row":16,"column":44},"action":"remove","lines":["t"]}],[{"start":{"row":16,"column":43},"end":{"row":16,"column":44},"action":"insert","lines":["p"],"id":23},{"start":{"row":16,"column":44},"end":{"row":16,"column":45},"action":"insert","lines":["r"]},{"start":{"row":16,"column":45},"end":{"row":16,"column":46},"action":"insert","lines":["o"]},{"start":{"row":16,"column":46},"end":{"row":16,"column":47},"action":"insert","lines":["d"]},{"start":{"row":16,"column":47},"end":{"row":16,"column":48},"action":"insert","lines":["u"]},{"start":{"row":16,"column":48},"end":{"row":16,"column":49},"action":"insert","lines":["c"]},{"start":{"row":16,"column":49},"end":{"row":16,"column":50},"action":"insert","lines":["t"]},{"start":{"row":16,"column":50},"end":{"row":16,"column":51},"action":"insert","lines":["s"]},{"start":{"row":16,"column":51},"end":{"row":16,"column":52},"action":"insert","lines":["."]},{"start":{"row":16,"column":52},"end":{"row":16,"column":53},"action":"insert","lines":["h"]}],[{"start":{"row":16,"column":53},"end":{"row":16,"column":54},"action":"insert","lines":["m"],"id":24},{"start":{"row":16,"column":54},"end":{"row":16,"column":55},"action":"insert","lines":["l"]}],[{"start":{"row":16,"column":55},"end":{"row":16,"column":56},"action":"insert","lines":[" "],"id":25},{"start":{"row":16,"column":56},"end":{"row":16,"column":57},"action":"insert","lines":["i"]},{"start":{"row":16,"column":57},"end":{"row":16,"column":58},"action":"insert","lines":["s"]}],[{"start":{"row":16,"column":58},"end":{"row":16,"column":59},"action":"insert","lines":[" "],"id":26},{"start":{"row":16,"column":59},"end":{"row":16,"column":60},"action":"insert","lines":["c"]},{"start":{"row":16,"column":60},"end":{"row":16,"column":61},"action":"insert","lines":["a"]},{"start":{"row":16,"column":61},"end":{"row":16,"column":62},"action":"insert","lines":["l"]},{"start":{"row":16,"column":62},"end":{"row":16,"column":63},"action":"insert","lines":["l"]},{"start":{"row":16,"column":63},"end":{"row":16,"column":64},"action":"insert","lines":["e"]},{"start":{"row":16,"column":64},"end":{"row":16,"column":65},"action":"insert","lines":["d"]}],[{"start":{"row":16,"column":65},"end":{"row":16,"column":66},"action":"insert","lines":[" "],"id":27},{"start":{"row":16,"column":66},"end":{"row":16,"column":67},"action":"insert","lines":["i"]},{"start":{"row":16,"column":67},"end":{"row":16,"column":68},"action":"insert","lines":["n"]},{"start":{"row":16,"column":68},"end":{"row":16,"column":69},"action":"insert","lines":["e"]}],[{"start":{"row":16,"column":68},"end":{"row":16,"column":69},"action":"remove","lines":["e"],"id":28}],[{"start":{"row":16,"column":68},"end":{"row":16,"column":69},"action":"insert","lines":["d"],"id":29},{"start":{"row":16,"column":69},"end":{"row":16,"column":70},"action":"insert","lines":["e"]},{"start":{"row":16,"column":70},"end":{"row":16,"column":71},"action":"insert","lines":["x"]}],[{"start":{"row":16,"column":71},"end":{"row":16,"column":72},"action":"insert","lines":[" "],"id":30}],[{"start":{"row":16,"column":71},"end":{"row":16,"column":72},"action":"remove","lines":[" "],"id":31}],[{"start":{"row":16,"column":71},"end":{"row":16,"column":72},"action":"insert","lines":["."],"id":32}],[{"start":{"row":16,"column":71},"end":{"row":16,"column":72},"action":"remove","lines":["."],"id":33}],[{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":34}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"insert","lines":["    "],"id":35}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["#"],"id":36}],[{"start":{"row":27,"column":5},"end":{"row":28,"column":53},"action":"insert","lines":["we can only adjust if a quantity is greater than 0.","If there's nothing in the cart, you cannot adjust it."],"id":37}],[{"start":{"row":27,"column":56},"end":{"row":27,"column":57},"action":"insert","lines":[" "],"id":38}],[{"start":{"row":27,"column":57},"end":{"row":28,"column":0},"action":"remove","lines":["",""],"id":39}],[{"start":{"row":13,"column":37},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":40},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]},{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""]},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":4},"end":{"row":19,"column":0},"action":"insert","lines":["if id in cart:","        cart[id] = int(cart[id]) + quantity      ","    else:","        cart[id] = cart.get(id, quantity) ",""],"id":41}],[{"start":{"row":14,"column":4},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":42},{"start":{"row":15,"column":0},"end":{"row":15,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["#"],"id":43}],[{"start":{"row":15,"column":5},"end":{"row":15,"column":181},"action":"insert","lines":["If the item is already in the cart, you want to add the new quantity to the existing quantity. However, if the item is not in the cart, then the current add_to_cart view works."],"id":44}],[{"start":{"row":15,"column":100},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":45},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["#"]}],[{"start":{"row":13,"column":4},"end":{"row":13,"column":37},"action":"remove","lines":["cart[id] = cart.get(id, quantity)"],"id":46}],[{"start":{"row":13,"column":4},"end":{"row":14,"column":4},"action":"remove","lines":["","    "],"id":47}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":86},"action":"remove","lines":["#However, if the item is not in the cart, then the current add_to_cart view works."],"id":48}],[{"start":{"row":15,"column":4},"end":{"row":16,"column":0},"action":"remove","lines":["",""],"id":49}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":8},"action":"remove","lines":["    "],"id":50}],[{"start":{"row":17,"column":9},"end":{"row":18,"column":0},"action":"insert","lines":["",""],"id":51},{"start":{"row":18,"column":0},"end":{"row":18,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":18,"column":8},"end":{"row":18,"column":90},"action":"insert","lines":["#However, if the item is not in the cart, then the current add_to_cart view works."],"id":52}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":100},"action":"remove","lines":["#If the item is already in the cart, you want to add the new quantity to the existing quantity. "],"id":53}],[{"start":{"row":12,"column":42},"end":{"row":13,"column":4},"action":"remove","lines":["","    "],"id":54}],[{"start":{"row":14,"column":18},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":55},{"start":{"row":15,"column":0},"end":{"row":15,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":104},"action":"insert","lines":["#If the item is already in the cart, you want to add the new quantity to the existing quantity. "],"id":56}]]},"timestamp":1568970076774}