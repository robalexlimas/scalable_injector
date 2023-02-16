#!/bin/bash
#
list=$(cat ./random.csv)
#
for i in $list
do
debug=$(echo $i|cut -f 1 -d ',')
enable=$(echo $i|cut -f 2 -d ',')
app=$(echo $i|cut -f 3 -d ',')
sm=$(echo $i|cut -f 4 -d ',')
sm_sub_core=$(echo $i|cut -f 5 -d ',')
core_type=$(echo $i|cut -f 6 -d ',')
core_id=$(echo $i|cut -f 7 -d ',')
in_out=$(echo $i|cut -f 8 -d ',')
operand=$(echo $i|cut -f 9 -d ',')
mask=$(echo $i|cut -f 10 -d ',')
stuckat=$(echo $i|cut -f 11 -d ',')
gpu=$(echo $i|cut -f 12 -d ',')
if [ ! -d /home/rlimassierra/FaultCampaing/$app/$gpu ]
then
mkdir -p /home/rlimassierra/FaultCampaing/$app/$gpu
fi
cat << EOF > /home/rlimassierra/FaultCampaing/$app/$gpu/$sm-$sm_sub_core-$core_type-$core_id-$in_out-$operand-$mask-$stuckat.sbatch
#!/bin/bash
#SBATCH --job-name=fault_campaing
#SBATCH --mail-type=ALL
#SBATCH --mail-user=robert.limassierra@polito.it
#SBATCH --partition=global
#SBATCH --time=00:01:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --output=$i.log
#SBATCH --mem-per-cpu=1024M
module purge
module load singularity/3.2.1
mkdir -p \$TMPDIR/$app/$gpu
singularity exec --bind \$TMPDIR/$app/$gpu:/injector/results /home/rlimassierra/FaultCampaing/injector.sif bash -c 'python /injector/python/app.py $debug $enable $app $sm $sm_sub_core $core_type $core_id $in_out $operand $mask $stuckat $gpu'
cp -r \$TMPDIR/$app/$gpu /home/rlimassierra/FaultCampaing/$app/$gpu
EOF
sbatch ./$app/$gpu/$sm-$sm_sub_core-$core_type-$core_id-$in_out-$operand-$mask-$stuckat.sbatch
done