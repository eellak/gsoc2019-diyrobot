module.exports = function(RED) {
    function AddPrefixSuffixNode(config) {
        RED.nodes.createNode(this,config);

	// code running inside node
	var node = this;
	node.prefix = config.prefix;
	node.suffix = config.suffix;
        
	node.on('input', function(msg) {
            msg.payload = node.prefix + msg.payload + node.suffix;
            node.send(msg);
        });
    }
    RED.nodes.registerType("add-prefix-suffix-node",AddPrefixSuffixNode);
}
