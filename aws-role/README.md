
A bash script to test AWS credentials

To use it in writing other scripts:

```bash
#!/bin/bash

aws-role >/dev/null
if [ "${?}" -eq 0 ]
then
    exit 1
fi
```

To run on console:

![aws-role](aws-role.png)

