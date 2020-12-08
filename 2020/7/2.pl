#!/opt/local/bin/perl
my %bags;
while(<>)
{
/(\w+\s\w+)+\sbags\scontain\s([\w\s\,]+?)\./;

$bags{$1} = $2;

$p1=$1;
$p2=$2;
#print "1: .$p1. .2: .$p2. \n";

# if(($c2 eq $c1))
# {print "jeppx.\n"}

}


#foreach my $bagc(keys %bags) {
#
#my $cols = $bags{$bagc};
#
# print "$bagc: $cols\n";
#if (cancarry($bagc)) {
# 	print "yes\n";
#	}
#}

$nn= contains ("shiny gold");

print "nn= $nn \n";

sub contains {
 my $inp=$_[0];
print "contains: $inp\n";
my $sum=0;
# if (index $bags{$_[0]}, "no other" >= 0) { return 1; }
foreach $i (split /,/, $bags{$_[0]})
{
$i =~/\s?(\d)\s(\w+\s\w+)/;
 my $num=$1;
$sum+=$num;
my $bc=$2;
print "fe:$inp $num $bc\n" ;
if ((index $bags{$bc}, "no other") >= 0) {  
#$sum += $num;
 }
else{
print "presum: $inp $sum\n";
$sum += $num * contains($bc);
print "sum: $inp :$bc $sum num:$num\n";
}
}
return $sum;
}


sub cancarry {
print "cc: $_[0]- $bags{$_[0]}\n";

my $noo = index  $bags{$_[0]},"no other";

print "ccn: $noo\n";

if ( $noo >= 0) { return 0; }

my $pi =  index $bags{$_[0]},"shiny gold";
# print "cc: $pi";
if ($pi > 0)
{
# print "ccyes";
	return 1;
	}

foreach $i (split /,/, $bags{$_[0]})
{
$i =~/\s?\d\s(\w+\s\w+)/; 
print "fe:$1\n";

if ( cancarry($1)){
   return 1;
   }
}
}
