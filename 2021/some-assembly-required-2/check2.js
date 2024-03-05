let exports;
(async()=>{
    let assembly = await fetch('./aD8SvhyVkb')
      , arraybuffer = await WebAssembly['instantiate'](await assembly['arrayBuffer']())
      , instance = arraybuffer['instance'];
    exports = instance['exports']];
}
)();
function onButtonPress() {
    let flag = 'flag'
    for (let i = 0x0; i < flag['length']; i++) {
        exports['copy_char'](flag['charCodeAt'](i), i);
    }
    exports['copy_char'](0x0, flag['length']),
    exports['check_flag']() == 0x1 ? document['getElementById']('result')['innerHTML'] = 'Correct!' : document['getElementById']('result')['innerHTML'] = 'Incorrect!';
}

