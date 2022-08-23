
What it does
Query the metadata of an GCE instance within GCP and provide a json formatted output.
The following Python sample shows how to programmatically watch the metadata server for changes.

About VM metadata 

Every virtual machine (VM) instance stores its metadata on a metadata server. Your VM automatically has access to the metadata server API without any additional authorization. Metadata is stored as key:value pairs.

VM instance metadata
The VM metadata entries are stored under the following directory:

http://metadata.google.internal/computeMetadata/v1/instance/

Instance attributes
Instance attributes are stored under the following directory:

http://metadata.google.internal/computeMetadata/v1/instance/attributes/

Instance guest attributes
Instance guest attributes are stored under the following directory:

http://metadata.google.internal/computeMetadata/v1/instance/guest-attributes

Every VM stores its metadata on a metadata server. Use these instructions to query these metadata values. For more information about metadata, see VM metadata.

Permissions
To query VM metadata, the following minimum permissions are required:

compute.projects.get on the project
compute.instances.get on the VM
You can also use a predefined role. To find predefined roles that contain these permissions, see Compute Engine IAM Roles.

Format query output
By default, each endpoint has a predefined format for the response. Some endpoints might return data in JSON format by default, while other endpoints might return data as a string. You can override the default data format specification by using the alt=json or alt=text query parameters, which return data in JSON string format or as a plain text representation, respectively.

For example, the tags key automatically returns data in JSON format. You can return data in text format instead, by specifying the alt=text query parameter.

